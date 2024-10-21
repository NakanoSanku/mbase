import json
from unittest import TestCase
from mbase.dataclass import Rect, RGB, Point


class TestPoint(TestCase):
    # 测试Point类
    def test_point_init(self):
        # 正确的初始化
        p = Point(1, 1)
        assert p.x == 1 and p.y == 1

        # 使用无值初始化
        with self.assertRaises(TypeError):
            p = Point()


        # 边界条件：非整数输入
        with self.assertRaises(TypeError):
            Point("1", 1)

        # 边界条件：负数输入
        with self.assertRaises(ValueError):
            Point(-1, 1)

    def test_point_is_in_rect(self):
        # 正确的矩形内判断
        rect = Rect(0, 0, 10, 10)  # 假设Rect类和下面的测试用例
        p = Point(5, 5)
        assert p.is_in_rect(rect)

        # 错误的矩形外判断
        rect = Rect(10, 10, 10, 10)
        p = Point(5, 5)
        assert not p.is_in_rect(rect)

    def test_point_offset(self):
        # 正确的偏移
        p = Point(1, 1)
        p_offset = p.offset(1, 1)
        assert p_offset.x == 2 and p_offset.y == 2

        # 边界条件：偏移量为负数
        p = Point(5, 5)
        p_offset = p.offset(-5, -5)
        assert p_offset.x == 0 and p_offset.y == 0

        # 边界条件：偏移量为零
        p = Point(1, 1)
        p_offset = p.offset()
        assert p_offset.x == 1 and p_offset.y == 1

class TestRect(TestCase):
    def setUp(self):
        self.rect1 = Rect(0, 0, 10, 10)
        self.rect2 = Rect(5, 5, 5, 5)
        self.rect3 = Rect(15, 15, 5, 5)

    def test_from_dict(self):
        d = {'x': 0, 'y': 0, 'w': 10, 'h': 10}
        rect = Rect.from_dict(d)
        self.assertEqual(rect, self.rect1)

    def test_to_dict(self):
        d = self.rect1.to_dict()
        self.assertDictEqual(d, {'x': 0, 'y': 0, 'w': 10, 'h': 10})

    def test_from_sequence(self):
        t = (0, 0, 10, 10)
        rect = Rect.from_sequence(t)
        self.assertEqual(rect, self.rect1)

    def test_to_sequence(self):
        t = self.rect1.to_sequence()
        self.assertTupleEqual(t, (0, 0, 10, 10))

    def test_from_json(self):
        j = json.dumps({'x': 0, 'y': 0, 'w': 10, 'h': 10})
        rect = Rect.from_json(j)
        self.assertEqual(rect, self.rect1)

    def test_to_json(self):
        j = self.rect1.to_json()
        self.assertEqual(j, json.dumps({'x': 0, 'y': 0, 'w': 10, 'h': 10}))

    def test_contains(self):
        self.assertTrue(self.rect1 in self.rect1)
        self.assertTrue(self.rect2 in self.rect1)
        self.assertFalse(self.rect3 in self.rect1)

    def test_type_error_in_contains(self):
        with self.assertRaises(TypeError):
            5 in self.rect1  # 尝试使用非Rect实例


class TestRGB(TestCase):

    def test_from_dict(self):
        # 测试RGB.from_dict方法
        d = {'r': 255, 'g': 165, 'b': 0}
        expected = RGB(255, 165, 0)
        actual = RGB.from_dict(d)
        self.assertEqual(actual, expected)

    def test_to_dict(self):
        # 测试RGB.to_dict方法
        expected = {'r': 255, 'g': 165, 'b': 0}
        actual = RGB(255, 165, 0).to_dict()
        self.assertEqual(actual, expected)

    def test_from_sequence(self):
        # 测试RGB.from_sequence方法
        t = (255, 165, 0)
        expected = RGB(255, 165, 0)
        actual = RGB.from_sequence(t)
        self.assertEqual(actual, expected)

        l = [255, 165, 0]
        expected = RGB(255, 165, 0)
        actual = RGB.from_sequence(l)
        self.assertEqual(actual, expected)

    def test_to_sequence(self):
        # 测试RGB.to_sequence方法
        expected = (255, 165, 0)
        actual = RGB(255, 165, 0).to_sequence()
        self.assertEqual(actual, expected)

    def test_from_json(self):
        # 测试RGB.from_json方法
        j = '{"r": 255, "g": 165, "b": 0}'
        expected = RGB(255, 165, 0)
        actual = RGB.from_json(j)
        self.assertEqual(actual, expected)

    def test_to_json(self):
        # 测试RGB.to_json方法
        expected = '{"r": 255, "g": 165, "b": 0}'
        actual = RGB(255, 165, 0).to_json()
        self.assertEqual(actual, expected)

    # 测试RGB类的is_similar方法
    def test_is_similar(self):
        # 创建两个相似的RGB实例
        color1 = RGB(255, 255, 255)
        color2 = RGB(254, 254, 254)

        # 验证这两个实例是否被认为是相似的（默认阈值）
        assert color1.is_similar(color2), "Expected the colors to be similar"

        # 创建两个不相似的RGB实例
        color3 = RGB(0, 0, 0)
        color4 = RGB(255, 0, 0)

        # 验证这两个实例是否被认为是不相似的（默认阈值）
        assert not color3.is_similar(color4), "Expected the colors to be dissimilar"

        # 测试阈值参数
        color5 = RGB(255, 255, 254)
        assert color1.is_similar(color5, threshold=2), "Expected the colors to be similar with threshold 2"

        # 测试阈值参数
        color6 = RGB(255, 255, 252)
        assert not color1.is_similar(color6, threshold=2), "Expected the colors to be similar with threshold 2"

        # 测试类型检查
        with self.assertRaises(TypeError):
            color1.is_similar("Not an RGB instance")

    def test_eq(self):
        # 测试RGB.__eq__方法
        self.assertTrue(RGB(255, 165, 0) == RGB(255, 165, 0))
        self.assertFalse(RGB(255, 165, 0) == RGB(255, 165, 1))

    def test_hex(self):
        # 测试RGB.__hex__方法
        expected = '#ffa500'
        actual = RGB(255, 165, 0).__hex__()
        self.assertEqual(actual, expected)

    def test_from_hex_valid(self):
        # 测试有效的16进制字符串
        hex_str = "#ff9100"
        rgb = RGB.from_hex(hex_str)
        self.assertEqual(rgb.r, 255)
        self.assertEqual(rgb.g, 145)
        self.assertEqual(rgb.b, 0)

    def test_from_hex_invalid(self):
        # 测试无效的16进制字符串
        hex_str = "ff91001"
        with self.assertRaises(ValueError):
            RGB.from_hex(hex_str)

    def test_to_hex(self):
        # 测试RGB对象转换为16进制字符串
        rgb = RGB(255, 145, 0)
        hex_str = rgb.to_hex()
        self.assertEqual(hex_str, "#ff9100")

    def test_from_int(self):
        # 测试从整数转换为RGB对象
        color_int = 0xff9100
        rgb = RGB.from_int(color_int)
        self.assertEqual(rgb.r, 255)
        self.assertEqual(rgb.g, 145)
        self.assertEqual(rgb.b, 0)

    def test_to_int(self):
        # 测试RGB对象转换为整数
        rgb = RGB(255, 145, 0)
        color_int = rgb.to_int()
        self.assertEqual(color_int, 0xff9100)

if __name__ == '__main__':
    from unittest import main
    main()
