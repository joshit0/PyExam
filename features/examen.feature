Feature: DemoBlaze
  Como cliente de Demoblaze
  Quiero seleccionar productos y realizar los flujos de compra
  Para realizar compras en la tienda online


  Scenario Outline: Agregar producto al carrito: <category> - <item>
    Given Abro la pagina de DemoBlaze
    And me logeo con mis credenciales
      | username   | password |
      | userjlqp01 | userpsw* |
    When selecciono categoria "<category>"
    And selecciono el producto "<item>"
    And agrego al carrito el item seleccionado
    Then muestra alerta con mensaje "product added."
    And veo el producto "<item>" en el carrito de compras
    Examples:
      | category | item              |
      | Phones   | Samsung galaxy s6 |
      | Laptops   | Sony vaio i5      |
      | Monitors  | Apple monitor 24  |



