import random


# 插入排序 从第二个值开始，与前面比较，如果比前面小就换值，从前面位置继续这个循环
def insert_sort(nums=None):
    if nums is None:
        nums = [random.randint(-100, 100) for _ in range(random.randint(10, 20))]
    elif not isinstance(nums, list):
        raise ValueError("输入参数必须是一个列表")
    elif not all(isinstance(num, (int, float)) for num in nums):
        raise ValueError("列表中的元素必须是整数或浮点数")

    for index in range(1, len(nums)):  # 第一个算有序，从第二个数开始
        tmpIndex = index  # 记录目前位置
        # 这个位置与前一个位置比较，大于或者等于前值就结束循环，小于前值就互换位置，
        # 继续从前一个位置执行判断，这样退出本次循环时tmpIndex之前的就是有序的
        # while tmpIndex > 0 and nums[tmpIndex] < nums[tmpIndex - 1]:
        #     nums[tmpIndex], nums[tmpIndex - 1] = nums[tmpIndex - 1], nums[tmpIndex]
        #     tmpIndex -= 1

        # 优化，不想每次都满足前大后小就交换值，只在最后一次满足条件后在执行
        currentValue = nums[index]
        while tmpIndex > 0 and currentValue < nums[tmpIndex - 1]:
            tmpIndex -= 1
        nums.insert(tmpIndex, nums.pop(index))
        # 其实没什么卵用，虽然下面的可以减少交换的次数，但是pop,insert本身也需要挪动数组的其他元素，两个操作也比较昂贵
    return nums


# 冒泡排序
def bubbling_sort(nums=None):
    if nums is None:
        nums = [random.randint(-100, 100) for _ in range(random.randint(10, 20))]
    elif not isinstance(nums, list):
        raise ValueError("输入参数必须是一个列表")
    elif not all(isinstance(num, (int, float)) for num in nums):
        raise ValueError("列表中的元素必须是整数或浮点数")

    n = len(nums)
    for i in range(n - 1):  # 前后比较，大的放后面，拿大的继续和后面的比较，外层控制循环次数
        for j in range(n - i - 1):  # 内层控制比较次数
            if nums[j] > nums[j + 1]:  # 前面比后面大,换
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    print(insert_sort())
    print(bubbling_sort())
