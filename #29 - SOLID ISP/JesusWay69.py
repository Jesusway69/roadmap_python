import os, platform
from abc import ABC, abstractmethod


if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" 
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta."""


class Bird (ABC):
    
    @abstractmethod
    def have_feathers():
        pass
    @abstractmethod
    def flies():
        pass
    @abstractmethod
    def swims():
        pass
    @abstractmethod
    def run():
        pass
    @abstractmethod
    def feature():
        return True
    

class Ostrich(Bird):
    def have_feathers():
        return super().feature()
    def flies():
        return False
    def swims():
        return False
    def run():
        return super().feature()
 
class Swift (Bird):
    def have_feathers():
        return super().feature()
    def flies():
        return super().feature()
    def swims():
        return False
    def run():
        return False

class Penguin (Bird):
    def have_feathers():
        return super().feature()
    def flies():
        return False
    def swims():
        return super().feature()
    def run():
        return False
    


class BirdISP(ABC):
    @abstractmethod
    def have_feathersISP(self):
        pass
    @abstractmethod
    def bird_name(self):
        pass
    def feature_ISP(self):
        return True
class FlyingBirdISP(ABC):
    @abstractmethod
    def flies_ISP(self):
        pass
class SwimmingBirdISP(ABC):
    @abstractmethod
    def swims_ISP(self):
        pass
class RunnerBirdISP(ABC):
    @abstractmethod
    def run_ISP(self):
        pass

class OstrichISP (BirdISP, RunnerBirdISP):
    def have_feathersISP(self):
        return super().feature_ISP()
    def run_ISP(self):
        return super().feature_ISP
    def bird_name(self):
        return "Avestruz"
class SwiftISP(BirdISP, FlyingBirdISP):
    def have_feathersISP(self):
        return super().feature_ISP()
    def flies_ISP():
        return super().feature_ISP()
    def bird_name(self):
        return "Vencejo"
class PenguinISP(BirdISP, SwimmingBirdISP, RunnerBirdISP):
    def have_feathersISP(self):
        return super().feature_ISP()
    def swims_ISP(self):
        return super().feature_ISP()
    def run_ISP(self):
        return super().feature_ISP
    def bird_name(self):
        return "Pingüino"
    
def test_birds(object):
    name = None
    feathers = False
    fly = False
    swim = False
    run = False
    if isinstance(object,OstrichISP):
        name = object.bird_name()
        feathers = object.have_feathersISP()
        run = object.run_ISP()
    elif isinstance(object, SwiftISP):
        feathers = object.have_feathersISP()
        name = object.bird_name()
        fly = object.flies_ISP()
    elif isinstance(object, PenguinISP):
        feathers = object.have_feathersISP()
        name = object.bird_name()
        swim = object.swims_ISP()
    print("\nEspecie de ave: " , name
                , "\n¿tiene plumas?: " , feathers
                , "\n¿Puede volar?: " , fly
                , "\n¿Puede correr?: " , run
                , "\n¿Puede nadar?: " , swim)

test_birds(OstrichISP())
    































    

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 *  Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio."""   