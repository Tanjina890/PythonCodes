#Task1
"""Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods"""
class Car():
      name=None
      model=None
      color=None
      engine=None
      price=None


      def speed(self):
          print(f"{self.name} {self.model} {self.color} in Color and Price {self.price} car speed is Good")
      def start_engine_sound(self):
          print("Sound effect is Awesome")
      def stop_engine(self):
          print(f"{self.engine} immediately stopped")
      def change_gear(self):
          print("No issue with Gear Changing")
      def parking(self):
          print("No  Problem")

lamborghini_obj=Car()
lamborghini_obj.name="Lamborghini"
lamborghini_obj.model="Aventador"
lamborghini_obj.color="White"
lamborghini_obj.engine="6.5 L V12"
lamborghini_obj.price="6 Lac"
print(lamborghini_obj)
lamborghini_obj.speed()
lamborghini_obj.start_engine_sound()
lamborghini_obj.stop_engine()
lamborghini_obj.change_gear()
lamborghini_obj.parking()

print("\n")

mahindra_obj=Car()
mahindra_obj.name="Mahindra"
mahindra_obj.model="XUV700"
mahindra_obj.color="Black"
mahindra_obj.engine="Straight Engine"
mahindra_obj.price="26Lac"
print(mahindra_obj)
mahindra_obj.speed()
mahindra_obj.start_engine_sound()
mahindra_obj.stop_engine()
mahindra_obj.change_gear()
mahindra_obj.parking()



print("\n")

#Task2
"""Create a Class Person,Two Objects by taking(name,age,address)input from users and print details in the end."""
class Person:
    name=None
    age=None
    address=None
    def person_details(self):
      print(f"I am {self.name},My age is {self.age},and I am from {self.address}")
person_name=input("Enter the Name:")
person_age=input("Enter the Age:")
person_address=input("Enter the Address:")

person1_obj=Person()
person1_obj.name=person_name
person1_obj.age=person_age
person1_obj.address=person_address
person1_obj.person_details()

person_name=input("Enter the Name:")
person_age=input("Enter the Age:")
person_address=input("Enter the Address:")

person2_obj=Person()
person2_obj.name=person_name
person2_obj.age=person_age
person2_obj.address=person_address
person2_obj.person_details()
