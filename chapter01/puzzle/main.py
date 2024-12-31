from troll import Troll
from axe_behavior import AxeBehavior
from knife_behavior import KnifeBehavior


if __name__ == "__main__":
    troll = Troll()
    troll.fight()

    axe = AxeBehavior()
    knife = KnifeBehavior()

    troll.set_weapon(axe)
    troll.weapon_behavior.use_weapon()
    troll.set_weapon(knife)
    troll.weapon_behavior.use_weapon()
