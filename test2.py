import cocos
from cocos.actions import ScaleBy, Repeat, Reverse


class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()
        label = cocos.text.Label(
            'Hello, world',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = 320, 240
        self.add(label)
        sprite = cocos.sprite.Sprite('airplane_710px_1219057_easyicon.net.png')
        sprite.position = 320, 240
        sprite.scale = 3
        self.add(sprite, z=1)
        scale = ScaleBy(3, duration=2)
        label.do(Repeat(scale + Reverse(scale)))
        sprite.do(Repeat(Reverse(scale) + scale))


cocos.director.director.init()
hello_layer = HelloWorld()
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)
