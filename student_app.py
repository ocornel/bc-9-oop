from student import Student


s1=Student('Qusai','Alfaki')
s2=Student('Ogendi','Ruth')
s3=Student('Muthui','Emmanuel')
s4=Student('Biwot','Kevin')
s5=Student('Gaamuwa','Samuel')
s6=Student('Cornel','Martin')
s7=Student('Mirriam','Amoit')
s8=Student('Gor','Micah')
s9=Student('Erick','Nyanamba')
s10=Student('Cecilia','Wambui')
s11=Student('Joan','Watiri')
    
s1.attend_class(date='Thu Aug 18 22:54:52 2016')
s2.attend_class(date='Thu Aug 18 22:54:52 2016')
s11.attend_class(date='Thu Aug 18 22:54:52 2016', teacher='Mwaleh')
s4.attend_class(date='Thu Aug 18 22:54:52 2016', teacher="Njira")
s10.attend_class(date='Thu Aug 18 22:54:52 2016', teacher='Nandaa')
    
print(s1.specific_day_attendees(date='Thu Aug 18 22:54:52 2016'))