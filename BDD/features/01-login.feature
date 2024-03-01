Feature: Automatización de acciones en la aplicación

  Scenario Outline: Iniciar Sesión
    Given que el usuario está en la página web de la aplicación Pais: "<country_code>" Brand: "<brand>"
    When el usuario hace clic en "Iniciar Sesión" e ingresa email: "<email>" y password: "<password>"


    Examples:
      | email                                        | password   | country_code | brand     |
      | cristian.depicciotto.qa.ar@balloon-group.com | Test123456 | AR           | Ensure    |
      | cristian.depicciotto.qa.pe@balloon-group.com | Test123456 | PE           | Pediasure |
      | cristian.depicciotto.qa.br@balloon-group.com | Test123456 | BR           | Glucerna  |
