import time

from behave import *
from BDD.pages.main_actions.addProductPage import addProduct


@when(u'el usuario agrega productos al carrito')
def step_impl(context):
    addProduct.addProduct(context)
    time.sleep(10)

@when(u'el carrito debería  productos agregados')
def step_impl(context):
    context.driver.refresh()
    addProduct.validate_shopping_cart(context)
