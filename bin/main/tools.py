import subprocess
import time

class General():
    def __init__(self):
        self.path = ""
        self.su_script_base = ""

    def wait(self):
        time.sleep(0.3)

    # removes extensions from file names
    def rm_extension(self, file_name):
        i = 0
        while i < len(file_name):
            if file_name[i] == ".":
                x = i
                break
            i = i + 1
        return file_name[:x]

    def read_test_script(self):
        f = open("test.sh", 'r')
        data = f.readlines()
        i = 3
        while i < len(data) - 1:
            print(">>")
            print(data[i].rstrip())
            i += 1

    # writes commands run under a module into history files
    def write_this(self, history, output_file, su_script_base):
        path = su_script_base + "history_cmd.txt"
        file = open(path, "a+")
        file.write("%s \n" % history)
        file.close()
        path2 = su_script_base + "history_file.txt"
        file = open(path2, "a+")
        file.write("%s \n" % (output_file))
        file.close()

    # copies a module script from scripts directory to temp file and replaces keyword "arg1" with "arg2" in temp file
    def load(self,original_file, arg1, arg2):
        with open("test.sh", 'w'): pass
        f1 = open(original_file, 'r')
        f2 = open('test.sh', 'a+')
        for line in f1:
            f2.write(line.replace(arg1, arg2))
        f1.close()
        f2.close()

    # change terminal directory to given path for data processing
    def change_dir(self,su_script_base, project_path):
        cd_path = su_script_base + "/cd.sh"
        self.load(cd_path, "path", project_path)
        subprocess.Popen(["bash", "test.sh"])

    # replaces "arg1" with "arg2" in temp file
    def assemble(self,arg1, arg2):
        f = open('test.sh', 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace(arg1, arg2)
        f = open('test.sh', 'w')
        f.write(newdata)
        f.close()

    # func. to make a new directory for new project

    # replaces characters in string2 with the ones in string 3 in string1,see uses in func. produce_opf_names
    def replace(self, string1, string2, string3):
        i = 0
        while i < len(string2):
            b = string2[i]
            for char in b:
                string1 = string1.replace(char, string3)
            i = i + 1
        return string1

    # produces output file names for su operations given some parameters
    def opf_names(self, parameters, input_file):
        self.opf = self.replace(parameters, "= ", "_") + "_" + input_file  # for commands like sugain and such others
        self.opf2 = self.replace(parameters, "= ", "_") + "_" + self.rm_extension(input_file)  # for viewing and exporting commands e.g. suxwigb
        return self.opf
    # copy file from one place to another

class Shell():
    def __init__(self):

        self.test = "test"

    def copy_file(self, source, destintation, bash_par=2):
        command = "cp " + source + " " + destintation
        self.bash(command, bash_par)
        print("Copied file : ", source)

    def make_dir(self, curr_dir, new_dir, bash_par=2):
        command = "cd " + curr_dir + "\n" + "mkdir " + new_dir
        self.bash(command, bash_par)
        print("Created Project directory : ", new_dir )

    def bash(self, command, bash_par):

        with open("test.sh", 'w'):
            pass
        file = open("test.sh", 'w')
        file.write(command)
        file.close()
        if bash_par == 1:
            subprocess.Popen(["bash", "test.sh"])
        elif bash_par == 2:
            print(command)
        elif bash_par == 3:
            print(command)
            subprocess.Popen(["bash", "test.sh"])
