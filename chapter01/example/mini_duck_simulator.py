from mallard_duck import MallardDuck
from model_duck import ModelDuck
from fly_rocket_powered import FlyRocketPowered


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered)
    model.perform_fly()
