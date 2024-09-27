Feature: Fluxo de Compras

    Scenario: O usuário seleciona um produto e o adiciona ao carrinho
        Given que eu estou na página de login
        When eu faço login com "standard_user" e "secret_sauce"
        Then eu devo ver a página de produtos
        And eu vejo o produto "Sauce Labs Backpack" com o preço "$29.99"
        When eu adiciono o produto ao carrinho
        Then o carrinho deve ter "1" item
        When eu visualizo o carrinho
        Then eu vejo que o carrinho contém "1" "Sauce Labs Backpack" com o preço "$29.99"
        When eu removo o produto do carrinho
        And eu faço logout