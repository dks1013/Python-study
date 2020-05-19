class AddressBook:
    person_list=[]

    def add(self, person):
        self.person_list.append(person)

    def show_all(self):
        for person in self.person_list:
            print(person.familyName + "" + person.name)

    def search(self, keyword):
        for person in self.person_list:
            if keyword in person.name or keyword in person.familyName:
                print(person.familyName + "" + person.name)

class Person:
    import datetime

    name=''         #이름
    familyName=''   #성
    phone=''        #전화번호
    email_Add=''    #메일 주소
    BirthDay=datetime.datetime(2000,1,1)    #생년월일

ab=AddressBook()
p=Person()
p.name='영희'
p.familyName='김'
p.phone='010-1234-5555'

ab.add(p)

p2=Person()
p2.name='찬호'
p2.familyName='박'
p2.phone='010-5678-9999'

ab.add(p2)

p3=Person()
p3.name='John'
p3.familyName='Lennon'
p3.phone='010-4587-7942'

ab.add(p3)

print("---동작확인---")
print("주소록에 등록된 사람 수 ->" +str(len(ab.person_list))+' 명')

print("===목록 표시===")
ab.show_all()

print("===검색===")
ab.search('김')


