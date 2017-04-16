from random import randint, shuffle, seed
from math import ceil, floor
from copy import deepcopy

class Genetic:
    inputs = []
    result = []

    def __init__(self):
        if(Jadwal.total_pasangan == 0):
            n = len(Jadwal.daftar_mata_kuliah)
            temp_total = 0
            for i in range(n):
                Jadwal.total_pasangan += temp_total * Jadwal.daftar_mata_kuliah[i].sks
                temp_total += Jadwal.daftar_mata_kuliah[i].sks
            Jadwal.total_pasangan += 1

    @classmethod
    def convertToMatriks(self, chromosome):
        M = Matriks(len(Jadwal.daftar_ruangan), 120)
        idx = 0
        for mkot in chromosome:

            awal = (mkot.h_selected-1) * 24 + (mkot.j_selected)
            for i in range(awal, awal + mkot.sks):
                M.matriks[mkot.r_selected][i].append(Jadwal.daftar_mata_kuliah[idx].nama)
            idx += 1
        return M

    @classmethod
    def fitness(self, chromosome):
        M = self.convertToMatriks(chromosome)
        con = int(M.conflict_count())
        return Jadwal.total_pasangan - int(M.conflict_count())

    # mutate ini dilakukan abis chromosomenya digabungin
    @classmethod
    def random_assign(self, x):

        bisa = False
        MBaru = MatKulOnlyTime(x)
        COMB_PER_HARI = Jadwal.daftar_mata_kuliah[x].jam_akhir - Jadwal.daftar_mata_kuliah[x].jam_awal - Jadwal.daftar_mata_kuliah[x].sks + 1
        JUMLAH_HARI = len(Jadwal.daftar_mata_kuliah[x].hari)
        comb_waktu = COMB_PER_HARI * JUMLAH_HARI
        urut_waktu = []
        for i in range(comb_waktu):
            urut_waktu.append(i)

        shuffle(urut_waktu)
        if(Jadwal.daftar_mata_kuliah[x].ruangan == '-'):
            urut_ruangan = []
            comb_ruangan = len(Jadwal.daftar_ruangan)

            for i in range(comb_ruangan):
                urut_ruangan.append(i)

            shuffle(urut_ruangan)
            for ruangan_selected in urut_ruangan:
                if bisa:
                    break
                for z in urut_waktu:
                    hari_selected = Jadwal.daftar_mata_kuliah[x].hari[floor(z / COMB_PER_HARI)]
                    jam_selected = Jadwal.daftar_mata_kuliah[x].jam_awal + (z % COMB_PER_HARI)
                    temp_ruangan = Jadwal.daftar_ruangan[ruangan_selected]
                    if(hari_selected in temp_ruangan.hari and jam_selected >= temp_ruangan.jam_awal and jam_selected + Jadwal.daftar_mata_kuliah[x].sks <= temp_ruangan.jam_akhir):
                        MBaru.setTime(ruangan_selected, jam_selected, hari_selected, Jadwal.daftar_mata_kuliah[x].sks)
                        break
        else:

            for idxruangan in range(len(Jadwal.daftar_ruangan)):
                assigned = False
                if(Jadwal.daftar_ruangan[idxruangan].nama == Jadwal.daftar_mata_kuliah[x].ruangan):
                    ruangan_selected = idxruangan
                    for z in urut_waktu:
                        hari_selected = Jadwal.daftar_mata_kuliah[x].hari[floor(z / COMB_PER_HARI)]
                        jam_selected = Jadwal.daftar_mata_kuliah[x].jam_awal + (z % COMB_PER_HARI)

                        temp_ruangan = Jadwal.daftar_ruangan[ruangan_selected]
                        if(hari_selected in temp_ruangan.hari and jam_selected >= temp_ruangan.jam_awal and jam_selected + Jadwal.daftar_mata_kuliah[x].sks <= temp_ruangan.jam_akhir):
                            MBaru.setTime(ruangan_selected, jam_selected, hari_selected, Jadwal.daftar_mata_kuliah[x].sks)
                            break
                    if assigned:
                        break
        return MBaru

    @classmethod
    def mutate(self, chromosome):
        panjang = len(chromosome)
        bnyk = int(ceil(panjang / 20))
        for i in range(bnyk):
            x = randint(0, panjang - 1)
            chromosome[x] = self.random_assign(x)

    @classmethod
    def selectidx(self, n, fitness_total, r_num):
        now = 0
        idx = 0
        for i in range(n):
            now += fitness_total[i]
            if(now > r_num):
                break
            idx += 1
        return idx

    @classmethod
    def run(self, loops):
        for xxx in range(loops):
            print (xxx)
            fitness_total = []
            n = len(self.inputs)

            # calculate total fitness
            for chromosome in self.inputs:
                fitness_total.append(self.fitness(chromosome))

            # sort based on fitness_total
            for i in range(n):
                for j in range(n-i-1):
                    if (fitness_total[j] > fitness_total[j+1]):
                        fitness_total[j], fitness_total[j+1] = fitness_total[j+1], fitness_total[j]
                        self.inputs[j], self.inputs[j+1] = self.inputs[j+1], self.inputs[j]

            pivot = randint(1, len(Jadwal.daftar_mata_kuliah))

            # calculate the total chance
            total_chance = 0
            for i in range(n):
                total_chance += fitness_total[i]

            self.result = []
            for i in range(n):
                x = self.inputs[self.selectidx(n, fitness_total, randint(0, total_chance-1))][:pivot]
                y = self.inputs[self.selectidx(n, fitness_total, randint(0, total_chance-1))][pivot:]
                child = x
                child.extend(y)
                if(n > randint(1, n*n)):
                    self.mutate(child)

                self.result.append(child)
            self.sort()
            self.result = deepcopy(self.result[91:])
            self.result.extend(self.inputs)
            self.sort()
            self.inputs = deepcopy(self.result[10:])

    @classmethod
    def init(self):
        seed()
        self.inputs = []
        self.result = []
        banyak = 100
        n = len(Jadwal.daftar_mata_kuliah)
        for i in range(banyak):
            self.inputs.append([])
            for x in range(n):
                self.inputs[i].append(self.random_assign(x))

    @classmethod
    def add(self, jadwal):
        self.inputs.append(jadwal)

    @classmethod
    def best(self):
        return self.result[-1]

    @classmethod
    def sort(self):
        fitness_total = []
        n = len(self.result)

        for chromosome in self.result:
            fitness_total.append(self.fitness(chromosome))

        for i in range(n):
            for j in range(n-i-1):
                if (fitness_total[j] > fitness_total[j+1]):
                    fitness_total[j], fitness_total[j+1] = fitness_total[j+1], fitness_total[j]
                    self.result[j], self.result[j+1] = self.result[j+1], self.result[j]

					
					
class Matriks:
    row = 0
    col = 0

    def __init__(self, r = None, c = None):
        if r is not None:
            self.row = r
        if c is not None:
            self.col = c

        self.matriks = []
        for i in range(self.row):
            self.matriks.append([])
            for j in range(self.col):
                self.matriks[i].append([])


    def conflict_count(self):
        total = 0
        for ruang in self.matriks:
            for jam in ruang:
                cnt = len(jam)
                total += cnt * (cnt-1) / 2
        return total

    def __str__(self):
        return (str(self.row) + ' ' + str(self.col) + ' ' + str(self.matriks))

		
		
class MatKulOnlyTime:
    def __init__(self, idmatkul):
        self.idmatkul = idmatkul
        self.r_selected = -1
        self.j_selected = -1
        self.h_selected = -1
        self.sks = -1

    def setTime(self, r, j, h, s):
        self.r_selected = int(r)
        self.j_selected = int(j)
        self.h_selected = int(h)
        self.sks = int(s)

    def __str__(self):
        return "Ruang : " + str(self.r_selected) + '\nHari : ' + str(self.h_selected) + '\nJam Mulai : ' + str(self.j_selected) + '\nSKS : ' + str(self.sks)

		
		
class MatKul:
    def __init__(self, idmatkul, nama, ruangan, awal, akhir, sks, hari):
        self.idmatkul = idmatkul
        self.nama = nama
        self.ruangan = ruangan
        self.jam_awal = awal
        self.jam_akhir = akhir
        self.sks = sks
        self.hari = hari

		
		
class Jadwal:
    daftar_ruangan = []
    daftar_mata_kuliah = []
    total_pasangan = 0

    @classmethod
    def process_ruangan_dan_mata_kuliah(self, ruangan_raw, mata_kuliah_raw):
        idruangan = 0
        for ruangan in ruangan_raw:
            temp = ruangan.split(';')
            temp[3] = temp[3].split(',')
            for i in range(len(temp[3])):
                temp[3][i] = int(temp[3][i])
            temp_ruangan = Ruangan(idruangan,temp[0], int(float(temp[1])), int(float(temp[2])), temp[3])
            idruangan += 1
            self.daftar_ruangan.append(temp_ruangan)

        idmatkul = 0
        for mata_kuliah in mata_kuliah_raw:
            temp = mata_kuliah.split(';')
            temp[5] = temp[5].split(',')
            for i in range(len(temp[5])):
                temp[5][i] = int(temp[5][i])
            temp_mata_kuliah = MatKul(idmatkul, temp[0], temp[1], int(float(temp[2])), int(float(temp[3])), int(temp[4]), temp[5])
            idmatkul += 1
            self.daftar_mata_kuliah.append(temp_mata_kuliah)

        n = len(self.daftar_mata_kuliah)
        temp_total = 0
        for i in range(0,n):
            self.total_pasangan += temp_total * self.daftar_mata_kuliah[i].sks
            temp_total += self.daftar_mata_kuliah[i].sks
        self.total_pasangan += 1

    @classmethod
    def read_file(self,ruangan_raw, mata_kuliah_raw, nama_file):
        f = open(nama_file, "r")
        mylist = f.read().splitlines()
        ruangan_loaded = False
        for line in mylist:
            if line == 'Ruangan' or line == '':
                pass
            elif line == 'Jadwal':
                ruangan_loaded = True
            elif not ruangan_loaded:
                ruangan_raw.append(line)
            else:
                mata_kuliah_raw.append(line)
        f.close()

    @classmethod
    def init_file(self,nama_file):
        ruangan_raw = []
        mata_kuliah_raw = []
        self.read_file(ruangan_raw, mata_kuliah_raw, nama_file)
        self.process_ruangan_dan_mata_kuliah(ruangan_raw, mata_kuliah_raw)

    @classmethod
    def __init__(self, nama_file):
        self.daftar_ruangan = []
        self.daftar_mata_kuliah = []
        self.init_file(nama_file)

		
		
class Assign:
	daftar_matkul_time = []

	@classmethod
	def hitung_kosong(cls, ruang, jam_awal, jam_akhir):
		selisih = jam_akhir - jam_awal
		hitung = 0
		for i in range(selisih):
			if len(cls.matriks.matriks[ruang][jam_awal+i]) == 0:
				hitung += 1
		return hitung

	@classmethod
	def min_kosong(cls, daftar):
		minim = 0
		for i in range(len(daftar)):
			if daftar[i] < daftar[minim]:
				minim = i
		return minim

	@classmethod
	def cariruang(cls, matkul):
		daftar_temp = []
		daftar_kosong = []
		temp_matkul_time = MatKulOnlyTime(matkul.idmatkul)
		if matkul.ruangan != '-': # ruangan udah ditentuin
			# tambahin looping aja didepannya
			for ruangan in Jadwal.daftar_ruangan:
				if ruangan.nama != matkul.ruangan:
					continue
				idx = ruangan.idruangan
				ruang = Jadwal.daftar_ruangan[idx]
				for hari in matkul.hari:
					for haris in ruang.hari:
						if hari == haris:
							if max(matkul.jam_awal, ruang.jam_awal) + matkul.sks <= min(matkul.jam_akhir, ruang.jam_akhir):
								temp_matkul_time.setTime(idx, max(matkul.jam_awal, ruang.jam_awal), hari, matkul.sks)
								kosong = cls.hitung_kosong(temp_matkul_time.r_selected, temp_matkul_time.j_selected, min(matkul.jam_akhir, ruang.jam_akhir))
								kosong = kosong - matkul.sks
								if kosong < 0:
									kosong = abs(kosong) + 100
								daftar_kosong.append(kosong)
								temp_masukin = deepcopy(temp_matkul_time)
								daftar_temp.append(temp_masukin)

		else:
			n = len(Jadwal.daftar_ruangan)
			for idx in range(n):
				ruang = Jadwal.daftar_ruangan[idx]
				for hari in matkul.hari:
					for haris in ruang.hari:
						if hari == haris:
							if max(matkul.jam_awal, ruang.jam_awal) + matkul.sks <= min(matkul.jam_akhir, ruang.jam_akhir):
								temp_matkul_time.setTime(idx, max(matkul.jam_awal, ruang.jam_awal), hari, matkul.sks)
								kosong = cls.hitung_kosong(temp_matkul_time.r_selected, temp_matkul_time.j_selected, min(matkul.jam_akhir, ruang.jam_akhir))
								kosong = kosong - matkul.sks
								if kosong < 0:
									kosong = abs(kosong) + 100
								daftar_kosong.append(kosong)
								temp_masukin = deepcopy(temp_matkul_time)
								daftar_temp.append(temp_masukin)
		if(len(daftar_temp) == 0):
			cls.daftar_remove.append(matkul)
		else:
			minim = cls.min_kosong(daftar_kosong)
			temp_matkul_time_final = daftar_temp[minim]
			cls.daftar_matkul_time.append(temp_matkul_time_final)

			c = (temp_matkul_time_final.h_selected - 1) * 24 + temp_matkul_time_final.j_selected
			for i in range(temp_matkul_time_final.sks):
				tempmatkul = deepcopy(matkul)
				cls.matriks.matriks[temp_matkul_time_final.r_selected][c+i].append(tempmatkul)

	@classmethod
	def __init__(cls):
		cls.daftar_remove = []
		cls.matriks = Matriks(len(Jadwal.daftar_ruangan), 120)
		cls.daftar_matkul_time = []
		for matkul in Jadwal.daftar_mata_kuliah:
			cls.cariruang(matkul)

		for matkul in cls.daftar_remove:
			Jadwal.daftar_mata_kuliah.remove(matkul)

		cnt = 0
		for matkul in Jadwal.daftar_mata_kuliah:
			matkul.idmatkul = cnt
			cnt += 1

			
			
class Ruangan:
    def __init__(self, idruangan, nama, jam_awal, jam_akhir, hari):
        self.idruangan = idruangan
        self.nama = nama
        self.jam_awal = jam_awal
        self.jam_akhir = jam_akhir
        self.hari = hari

		
Jadwal('SourcePythonTubesAIRadit/Testcases/m1_abnormal.txt')		
Assign()
Genetic()
Genetic.init()
Genetic.add(Assign.daftar_matkul_time)
Genetic.run(100)
Genetic.sort()
M = Genetic.convertToMatriks(Genetic.best())
for i in range(M.row):
	for j in range(M.col):
		print (M.matriks[i][j], end='')
	print()
	print()