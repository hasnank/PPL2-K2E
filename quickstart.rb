require 'google/apis/calendar_v3'
require 'googleauth'
require 'googleauth/stores/file_token_store'

require 'fileutils'
require 'certified'
require 'json'

OOB_URI = 'urn:ietf:wg:oauth:2.0:oob'
APPLICATION_NAME = 'Google Calendar API Ruby Quickstart'
CLIENT_SECRETS_PATH = 'client_secret.json'
CREDENTIALS_PATH = File.join(Dir.home, '.credentials',
                             "calendar-ruby-quickstart.yaml")
SCOPE = Google::Apis::CalendarV3::AUTH_CALENDAR_READONLY

##
# Ensure valid credentials, either by restoring from the saved credentials
# files or intitiating an OAuth2 authorization. If authorization is required,
# the user's default browser will be launched to approve the request.
#
# @return [Google::Auth::UserRefreshCredentials] OAuth2 credentials
def authorize
  FileUtils.mkdir_p(File.dirname(CREDENTIALS_PATH))

  client_id = Google::Auth::ClientId.from_file(CLIENT_SECRETS_PATH)
  token_store = Google::Auth::Stores::FileTokenStore.new(file: CREDENTIALS_PATH)
  authorizer = Google::Auth::UserAuthorizer.new(
    client_id, SCOPE, token_store)
  user_id = 'default'
  credentials = authorizer.get_credentials(user_id)
  if credentials.nil?
    url = authorizer.get_authorization_url(
      base_url: OOB_URI)
    puts "Open the following URL in the browser and enter the " +
         "resulting code after authorization"
    puts url
    code = gets
    credentials = authorizer.get_and_store_credentials_from_code(
      user_id: user_id, code: code, base_url: OOB_URI)
  end
  credentials
end

# Initialize the API
service = Google::Apis::CalendarV3::CalendarService.new
service.client_options.application_name = APPLICATION_NAME
service.authorization = authorize

# Fetch the next 10 events for the user
calendar_id = 'ikhwan.m1996@gmail.com'
response = service.list_events(calendar_id,
                               max_results: 10,
                               single_events: true,
                               order_by: 'startTime',
                               time_min: Time.now.iso8601)
puts "Wawawaw"
puts (response.to_json)
myjson = {}
myjson["data"] ||= []
tempjson = {}
id = 0
puts "No upcoming events found" if response.items.empty?
response.items.each do |event|
  id = id + 1
  tempjson["id"] ||= {}
  tempjson["id"] = id
  tempjson["text"] ||= {}
  tempjson["text"] = "#{event.summary}"

  startDate = Date.strptime("#{event.start.date_time}", '%FT%T%:z').strftime("%m-%d-%Y %T")
  endDate = Date.strptime("#{event.end.date_time}", '%FT%T%:z').strftime("%m-%d-%Y %T")

  tempjson["start_date"] ||= {}
  tempjson["start_date"] = startDate
  tempjson["end_date"] ||= {}
  tempjson["end_date"] = endDate
  myjson["data"] << tempjson.clone
  puts JSON.dump(tempjson)
  puts "*****************************"
  puts JSON.dump(myjson)
  puts "*****************************"
end

puts "============================="
puts "============================="
puts "============================="
puts JSON.dump(myjson)
File.open("jadwal.json", 'w') {
 |file| file.write( JSON.dump(myjson)) 
}

