import enum
Season = enum.Enum(Season, ('SPRING', 'SUMMER', 'Fall', 'WINTER'))
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)