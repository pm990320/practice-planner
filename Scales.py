import pypyodbc
import random
import sys

class Scales:
    scales = []
    contrary_motions = []
    other_technical_exercises = []
    arpeggios = []

    note_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    accidentals = ['', '#', 'b']
    hands = ['left hand', 'right hand', 'hands together']
    
    def __init__(self):
        # establish connection with database
        connection_string = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\\Users\\Patrick\\Documents\\PROGRAMMING\\PYTHON\\PracticePlanner\\Piano.mdb'
        conn = pypyodbc.connect(connection_string)
        cur = conn.cursor()
        
        # get scales
        cur.execute('SELECT ScaleName FROM ScaleTable')
        for row in cur.fetchall():
            for field in row:
                self.scales.append(field)

        # get contrary motions
        cur.execute('SELECT ContraryMotionName FROM ContraryMotionTable')
        for row in cur.fetchall():
            for field in row:
                self.contrary_motions.append(field)

        # get other technical exercises
        cur.execute('SELECT TechnicalExerciseName FROM TechnicalExerciseTable')
        for row in cur.fetchall():
            for field in row:
                self.other_technical_exercises.append(field)

        # get arpeggios
        cur.execute('SELECT ArpeggioName FROM ArpeggioTable')
        for row in cur.fetchall():
            for field in row:
                self.arpeggios.append(field)

    def getScale(self):
        return 'Scale of ' + random.choice(self.scales) + ', ' + random.choice(self.hands)

    def getArpeggio(self):
        return 'Arpeggio of ' + random.choice(self.arpeggios) + ', ' + random.choice(self.hands)

    def getContraryMotion(self):
        return random.choice(self.contrary_motions)

    def getChromatic(self):
        return 'Chromatic scale beginning on ' + random.choice(self.note_names) + random.choice(self.accidentals) + ', ' + random.choice(self.hands)

    def getTechnicalExercise(self):
        return random.choice(self.other_technical_exercises)

    def printout(self):
        # print out the random choices however you want...
        print("\n\nBegin your practice with these technical exercises: \n")

        i = 0
        while i != 5:
            print self.getScale()
            i += 1
        print ''

        i = 0
        while i != 5:
            print self.getArpeggio()
            i += 1
        print ''

        i = 0
        while i != 2:
            print self.getContraryMotion()
            i += 1
        print ''

        i = 0
        while i != 2:
            print self.getChromatic()
            i += 1
        print ''

        print "\nNow do 3 sight reading exercises then move on to your pieces \nRemember to learn parts of pieces by playing them slowly \n"

        var = input("Are you finished? [Y/n] ")
