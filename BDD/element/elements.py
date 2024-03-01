elements = {
    "logIn": [
        "//span[@id='myaccount-span']",
        "//span[@id='myaccount-span']//..//..//..//li[@class='authorization-link']",
        "//input[@id='email']",
        "//input[@id='pass']",
        "//button[@class='action login primary']"],

    "addProduct": [
        "(//h2//..//..//..//..//div[@class='item product product-item'])[",
        "(//div[@class='qty-changer']//a[@class='qty-inc']//i[@class='porto-icon-up-dir'])[2]",
        "(//div[@class='qty-changer']//a[@class='qty-dec'])[2]",
        "//button[@class='action primary tocart']"

    ],
    "open-cart": ["//a[@class='action showcart']",
                  "//button[@id='top-cart-btn-checkout']",
                  ]

}
