
from kivy.lang import Builder
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivymd.app import MDApp
from matplotlib import pyplot as plt

KV = '''
Screen:
    BoxLayout:
        orientation: "horizontal"
        spacing: "20dp"
        MDFloatLayout:
            radius: [0,25, 0, 0]
            orientation:'vertical'
            size_hint:.2,1
            md_bg_color: app.theme_cls.primary_color
            MDFillRoundFlatIconButton:
                size_hint:.8,.08
                icon: "android"
                text: "addmore"
                pos_hint: {"center_x": .4, "center_y": .9}
                md_bg_color: 1, 0, 1, 1
            MDFillRoundFlatIconButton:
                size_hint:.8,.08
                icon: "android"
                text: "buy now"
                pos_hint: {"left":.3, "center_y": .8}
                md_bg_color: 1, 0, 1, 1
            MDFillRoundFlatIconButton:
                size_hint:.8,.08
                icon: "android"
                text: "gift more"
                pos_hint: {"left":.4, "center_y": .7}
                md_bg_color: 1, 0, 1, 1
        MDBoxLayout:
            orientation:"vertical"
            size_hint:.8,1
            spacing: "10dp"
            padding: "10dp"
            MDCard:
                padding: "4dp"
                orientation: "horizontal"
                padding: "20dp"
                size_hint:1,.2
                radius:[20]
                pos_hint: {"left": .5, "center_y": .6}
                MDBoxLayout:
                    orientation:"horizontal"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint:.25,1
                    spacing: "10dp"
                    MDIcon:
                        size_hint:.1,.3
                        icon: "cash.png"
                        pos_hint: {"left": .3, "center_y": .6}
                    MDBoxLayout:
                        size_hint:.4,.4
                        pos_hint: {"left": .5, "center_y": .6}
                        orientation:"vertical"
                        MDLabel:
                            font_size: dp(10)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Total Sell"
                        MDLabel:
                            font_size: dp(10)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "$1290"

                MDBoxLayout:
                    orientation:"horizontal"
                    pos_hint: {"left": .5, "center_y": .5}
                    size_hint:.25,1
                    spacing: "10dp"
                    MDIcon:
                        size_hint:.1,.3
                        icon: "cash.png"
                        pos_hint: {"left": .3, "center_y": .6}
                    MDBoxLayout:
                        size_hint:.4,.4
                        pos_hint: {"left": .5, "center_y": .6}
                        orientation:"vertical"
                        MDLabel:
                            font_size: dp(10)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Unit Cost"
                        MDLabel:
                            font_size: dp(10)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "$12.5"

                MDBoxLayout:
                    orientation:"horizontal"
                    pos_hint: {"left": .5, "center_y": .5}
                    size_hint:.25,1
                    spacing: "10dp"
                    MDIcon:
                        size_hint:.1,.3
                        icon: "cash.png"
                        pos_hint: {"left": .3, "center_y": .6}
                    MDBoxLayout:
                        size_hint:.4,.4
                        pos_hint: {"left": .5, "center_y": .6}
                        orientation:"vertical"
                        MDLabel:
                            font_size: dp(10)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Total VAT"
                        MDLabel:
                            font_size: dp(10)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "1.2%"

                MDBoxLayout:
                    orientation:"horizontal"
                    pos_hint: {"left": .5, "center_y": .5}
                    size_hint:.25,1
                    spacing: "10dp"
                    MDIcon:
                        size_hint:.1,.3
                        icon: "cash.png"
                        pos_hint: {"left": .3, "center_y": .6}
                    MDBoxLayout:
                        size_hint:.4,.4
                        pos_hint: {"left": .5, "center_y": .6}
                        orientation:"vertical"
                        MDLabel:
                            font_size: dp(10)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Total products(stock)"
                        MDLabel:
                            font_size: dp(10)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "430"

            MDBoxLayout:
                orientation:"horizontal"
                spacing: "10dp"
                size_hint:1,.6
                padding: "10dp"
                MDCard:
                    size_hint:.5, None
                    radius:[20]
                    orientation:"horizontal"
                    size_hint:.9,.8
                    MDBoxLayout:
                        orientation:"vertical"
                        padding_bottom:'10dp'
                        size_hint:.7,.7
                        pos_hint: {"left": .3, "center_y": .5}
                        id:m1
                    MDBoxLayout:
                        orientation:"vertical"
                        size_hint:.4,.4
                        pos_hint: {"left": .2, "center_y": .5}
                        MDLabel:
                            font_size: dp(15)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Stock Record  23% "
                            theme_text_color: "Custom"
                            text_color: 1, .3058823,.3058823,1
                        MDLabel:
                            font_size: dp(15)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Sales increase  33% "
                            theme_text_color: "Custom"
                            text_color: .01176470, .9333333,.8627450,1
                        MDLabel:
                            font_size: dp(15)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Total sales increase 39%"
                            theme_text_color: "Custom"
                            text_color: 0, .678431,.9725490,1
                        MDLabel:
                            font_size: dp(15)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Return Amount Increase 18%"
                            theme_text_color: "Custom"
                            text_color: 1, .5882352,.3215686,1
                        
                MDCard:
                    size_hint:.5, None
                    radius:[20]
                    size_hint:.9,.8
                    MDBoxLayout:
                        size_hint:.8,.8
                        padding_right:'10dp'
                        pos_hint: {"center_x": .4, "center_y": .5}
                        id:m
                   
            MDBoxLayout:
                orientation:"horizontal"
                spacing: "10dp"
                size_hint:1,.2
                MDCard:
                    padding: "4dp"
                    orientation: "horizontal"
                    padding: "8dp"
                    size_hint:.4,1
                    radius:[20]
                    pos_hint: {"left": .5, "center_y": .5}
                    MDBoxLayout:
                        orientation:"vertical"
                        size_hint:.4,.4
                        pos_hint: {"left": .2, "center_y": .5}
                        MDLabel:
                            font_size: dp(15)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Stock Record  23% "
                            theme_text_color: "Custom"
                            text_color: .1529411, .3058823,.3058823,1
                        MDLabel:
                            font_size: dp(15)
                            pos_hint: {"left": .5, "center_y": .6}
                            text: "Sales increase  33% "
                            theme_text_color: "Custom"
                            text_color: .01176470, .9333333,.8627450,1
                MDCard:
                    padding: "4dp"
                    orientation: "horizontal"
                    padding: "8dp"
                    size_hint:.6,1
                    radius:[20]
                    pos_hint: {"left": .5, "center_y": .5}
                    MDBoxLayout:
                        orientation:"horizontal"
                        MDBoxLayout:
                            orientation:"vertical"
                            size_hint:.4,.4
                            pos_hint: {"left": .2, "center_y": .5}
                            MDLabel:
                                font_size: dp(15)
                                pos_hint: {"left": .5, "center_y": .6}
                                text: "Stock Record  23% "
                                theme_text_color: "Custom"
                                text_color: 1,0,1,1
                            MDLabel:
                                font_size: dp(15)
                                pos_hint: {"left": .5, "center_y": .6}
                                text: "Sales increase  33% "
                                theme_text_color: "Custom"
                                text_color: .1529411, .3058823,.3058823,1
                        MDBoxLayout:
                            orientation:"vertical"
                            size_hint:.4,.4
                            pos_hint: {"left": .2, "center_y": .5}
                            MDLabel:
                                font_size: dp(15)
                                pos_hint: {"left": .5, "center_y": .6}
                                text: "Stock Record  23% "
                                theme_text_color: "Custom"
                                text_color: 1,0,1,1
                            MDLabel:
                                font_size: dp(15)
                                pos_hint: {"left": .5, "center_y": .6}
                                text: "Sales increase  33% "
                                theme_text_color: "Custom"
                                text_color: .1529411, .3058823,.3058823,1
'''



class TestCard(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen

    def on_start(self):
        '''Creates a list of cards.'''

        plt.plot([1, 23, 2, 4,4,5,6,3,2,5,6,8,3],color='lightcoral', linewidth=4)
        plt.ylabel('Sales increase per month')
        self.screen.ids.m.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        '''Creates a list of cards.'''
        # Pie chart
        sizes = [15, 30, 45, 10]
        # colors
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        plt1 = plt
        fig1, ax1 = plt1.subplots()
        ax1.pie(sizes, colors=colors, startangle=90)
        # draw circle
        centre_circle = plt1.Circle((0, 0), 0.80, fc='white')
        fig = plt1.gcf()
        fig.gca().add_artist(centre_circle)
        # Equal aspect ratio ensures that pie is drawn as a circle
        self.screen.ids.m1.add_widget(FigureCanvasKivyAgg(plt.gcf()))


TestCard().run()
