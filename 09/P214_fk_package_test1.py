import fk_package
import fk_package.P214_print_shape
from fk_package import P214_billing
import fk_package.P213_arithmetic_chart

fk_package.P214_print_shape.print_blank_triangle(5)
im = P214_billing.Item(4.5)
print(im)
fk_package.P213_arithmetic_chart.print_multiple_chart(5)