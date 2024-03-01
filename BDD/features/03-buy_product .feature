Feature: Compras en una tienda en línea

  Scenario Outline: Agregar productos al carrito
    Given que el usuario está en la página web de la aplicación Pais: "<country_code>" Brand: "<brand>"
    When el usuario hace clic en "Iniciar Sesión" e ingresa email: "<email>" y password: "<password>"
    When el usuario agrega productos al carrito
    When el carrito debería  productos agregados

    Examples:
      | email                                        | password   | country_code | brand     |
      | cristian.depicciotto.qa.pe@balloon-group.com | Test123456 | PE           | Pediasure |
      | cristian.depicciotto.qa.br@balloon-group.com | Test123456 | BR           | Glucerna  |
