from pprint import pprint

def read_grades(filename):

    grade_list = []

    tf = open(filename, "r")
    line = tf.readline()
    
    for line in tf:
        values = line.strip().split("\t")

        grade_list.append(values)
        
        if line == "":
            break

    tf.close()
    return grade_list
    

def main():
    pprint(read_grades("grades.tsv"))

main()