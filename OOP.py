# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:42:26 2023

@author: Sh_Jurayeff
"""
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.kurs = 1
      
#     def set_kurs(self,kurs):
#         """Talabaning kursini yangilovchi metod"""
#         self.kurs = kurs
        
#     def update_kurs(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.kurs += 1    
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.kurs}-bosqich talabasi "
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self,yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil
    
# class Fan():
#     """Fan nomli klass"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [talaba.get_info() for talaba in self.talabalar]
    
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni 


#class User:
#     def __init__(self,ism,familiya,username,tyil,email,telefon_number):
#         self.ism=ism
#         self.familiya=familiya
#         self.username=username
#         self.email=email
#         self.telefon_number=telefon_number
#         self.tyil=tyil
        
#     def get_age (self):
#         return self.tyil 
    
#     def get_info(self):
#         return f" {self.ism}  {self.familiya} {self.tyil} - yilda tug'ilgan. Email: {self.email}. Telefon raqami: {self.telefon_number}."
    
# user1 = User("Sherali", "Jo'rayev", "Sh_jurayeff", 2002, "sh_jurayeff@gmail.com", "906677664")  



# class Avto :
#     def __init__(self,model, rang, korobka, narh , kilometr = 0 ) : 
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.rang = rang
        
#     def get_info(self):
#         return f"Model: {self.model} , Rangi : {self.rang} , Karobka : {self.korobka} , Narh: {self.narh} , Kilometr: {self.kilometr}"
    
#     def update_kilometr(self,km):
#         return km
        
# class Avtosalon:
#     def __init__(self,salon_name,adress):
#         self.salon = salon_name
#         self.adress = adress
#         self.buy_avtos = []
#         self.avto_soni = 0

#     def add_avtos(self,new_car):
#         self.buy_avtos.append(new_car)
#         self.avto_soni +=1
        
#     def get_avto(self):
#         return  [avto.get_info() for avto in  self.buy_avtos ]
    
#     def see_methods(klass):
#         return [method for method in dir (klass) if method.startswith('__') is False]
             
# avto1 = Avto("Gentra", "Black", "Avtomat", 17000 , 0)     
# avto2 = Avto("Nexia", "White", "Avtomat", 11000 , 0)   
   ############## VORISLIK ##################       
# class Shaxs:  #-->> SUPER CLASS
#     def __init__(self,ism,familiya,passport,tyil ):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#         self.bosqich = 1 
        
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}. "
#         info+= f"Passport: {self.passport} {self.tyil}-da tug'ilgan"   
#         return info
    
#     def get_age(self,hozirgi_yil):
#         return hozirgi_yil-self.tyil
    
    
# class Talaba(Shaxs):  #--->>> VORIS CLASS
#     def __init__(self, ism, familiya, passport, tyil ,idraqam,manzil) :
#         super().__init__(ism, familiya, passport, tyil)         
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
        
#     def get_id(self):
#         return self.idraqam

#     def get_bosqich(self):
#         return self.bosqich            
        
#     def get_info(self): #---->>>>>>>>> Polimorfizm
#         info = f"{self.ism} {self.familiya}."
#         info+= f"{self.get_bosqich()} - bosqich. ID : {self.get_id()} "
#         return info
# class Manzil:
#     def __init__ (self,viloyat,tuman,mahalla,kocha,uy):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.mahalla = mahalla
#         self.kocha = kocha
#         self.uy = uy

#     def get_manzil(self):
#         manzil = f"{self.viloyat} viloyati , {self.tuman} tumani , "
#         manzil+= f" {self.mahalla} mahallasi, "
#         manzil+= f"{self.kocha} ko'chasi , {self.uy} - uy."
#         return manzil
                
# talaba1_manzil = Manzil("Qashqadaryo", "Kitob", "Qalmoq", "Gulzor", 50)
# talaba1 = Talaba("Dima", "Abdiyev", "WW1212121212", 2002, "ID232323",talaba1_manzil )        
        
from uuid import uuid4

class Avto :
    __num_avto = 0 
    def __init__(self,make, model,rang,yil,narx,km):
        self.make = make
        self.model = model 
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km 
        self.__id = uuid4()  
        Avto.__num_avto += 1
        
    @classmethod    
    def get_num_avto(cls):
        return cls.__num_avto
        
    def get_km(self):
        return   self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km>=0:
            self.__km+=km
        else:
            print("Mashina km ni kamaytirib bo'lmaydi")    
        

        
        
        
        









































































        
