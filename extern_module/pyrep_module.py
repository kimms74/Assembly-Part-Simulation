from os.path import join
from socket import *

from pyrep import PyRep

from script.fileApi import *
from script.const import SockType



def request_assembly_region(group_info, target):
    pass


class InstructionScene(object):
    def __init__(self, group_info_path):
        self.group_info = load_yaml_to_dic(group_info_path)

        self.pr = PyRep()
        self.pr.launch()
        self.pr.start()

        self.load_group_objects_to_scene()

    def load_group_objects_to_scene(self):
        group_objects = {}
        for group_name in self.group_info.keys():
            obj_root = self.group_info[group_name]["obj_root"]
            group_objects[group_name] = GroupObject(obj_root, pr)

        return group_objects

def import_group_object_to_scene(obj_root, scene):
    


if __name__ == "__main__":
    
    port = 8081

    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', port))

    print("[CoppeliaSim] Start Module")
    while True:
        data = clientSock.recv(1024).decode('utf-8')
        if data == SockType.start_instruction_step.value:
            print("[CoppeliaSim] Ready to simulate instruction step")
            while True:
                data = clientSock.recv(1024).decode('utf-8')
                if data == SockType.end_instruction_step.value:
                    print("[CoppeliaSim] End to simulate instruction step")
                    break
                print(data)
                
        elif data == SockType.end_assembly.value:
            break
        
        else:
            pass
    print("[CoppeliaSim] End Module")
    clientSock.close()
        
    