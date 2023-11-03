class Package():
    def __init__(self, package_name, package_reference):
        self.package_name = package_name
        self.package_reference = package_reference
list_packages = []
with open('client-package.txt','r', encoding='utf8') as packages:
    for package in packages:
        package_name, package_reference = package.strip().split()
        list_packages.append(Package(package_name, package_reference))

sorted_packages = sorted(list_packages, key=lambda obj: obj.package_name)
print('Beautify command')
print('npm install -save', end=' ')
for package in sorted_packages:
    print(package.package_name, end=' ')
print('\nรายละเอียด')
for package in sorted_packages:
    print('ชื่อแพ็กเกจ:', package.package_name)
    print('แหล่งอ้างอิง:', package.package_reference)
