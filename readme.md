# `mbase` 
用于`minifw`基本模块
定义通用数据结构，常用的工具函数等

## Point 类
表示二维坐标点。

### 方法
- **is_in_rect(rect: Rect) -> bool**: 判断点是否在指定矩形内。
- **offset(dx: int = 0, dy: int = 0) -> Point**: 返回偏移后的新点。

## Rect 类
表示矩形区域。

### 属性
- **x**: 矩形左上角的 x 坐标。
- **y**: 矩形左上角的 y 坐标。
- **w**: 矩形的宽度。
- **h**: 矩形的高度。

### 方法
- **from_dict(d: dict) -> Rect**: 从字典创建 Rect 实例。
- **to_dict() -> dict**: 将 Rect 转换为字典。
- **from_sequence(t: Union[list[int, int, int, int], tuple[int, int, int, int]]) -> Rect**: 从列表或元组创建 Rect。
- **to_sequence() -> tuple[int, int, int, int]**: 将 Rect 转换为元组。
- **from_json(j: str) -> Rect**: 从 JSON 字符串创建 Rect。
- **to_json() -> str**: 将 Rect 转换为 JSON 字符串。
- **center() -> Point**: 返回矩形的中心点。
- **__contains__(item: Rect) -> bool**: 判断一个矩形是否包含另一个矩形。

## RGB 类
表示 RGB 颜色。

### 方法
- **from_dict(d: dict) -> RGB**: 从字典创建 RGB 实例。
- **to_dict() -> dict**: 将 RGB 转换为字典。
- **from_sequence(t: Union[list[int, int, int], tuple[int, int, int]]) -> RGB**: 从列表或元组创建 RGB。
- **to_sequence() -> tuple[int, int, int]**: 将 RGB 转换为元组。
- **from_json(j: str) -> RGB**: 从 JSON 字符串创建 RGB。
- **to_json() -> str**: 将 RGB 转换为 JSON 字符串。
- **is_similar(other: RGB, threshold: int = 4) -> bool**: 判断两个 RGB 是否相似。

## Size 类
表示大小。

### 属性
- **width**: 宽度。
- **height**: 高度。
