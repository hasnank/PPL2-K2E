require 'darwinning'

class GeneticAlgorithm
  include Darwinning

  GENE_RANGES = {
      ruangan: ('7602', '7606'),
      jam: (7..18),
      dosen: ('pak', 'bu kamu'),
      mahasiswa: ('aku', 'kamu', 'kita')
  }

  attr_accessor :ruangan, :jam, :dosen, :mahasiswa

  def fitness
    # Try to get the sum of the 3 digits to add up to 100
    (first_number + second_number + third_number - 100).abs
  end

end

if GeneticAlgorithm.is_evolveable?
  triple_pop = GeneticAlgorithm.build_population(0, 10, 100)
  triple_pop.evolve! # evolve until fitness goal is or generations limit is met

  puts "Best member: #{triple_pop.best_member}"
end