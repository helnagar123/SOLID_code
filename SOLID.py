from abc import ABC, abstractmethod


class Product:
    """Represents a product with a name and price."""
    def _init_(self, name: str, price: float):
        self.name = name
        self.price = price
        

class Cart:
    """Manages a list of products in the cart."""
    def _init_(self):
        self.products: list[Product] = []  

    def add_product(self, product: Product):
        self.products.append(product)

    def get_total_price(self) -> float:
        return sum(product.price for product in self.products)


class DiscountStrategy(ABC):
    """Abstract base class for discount strategies."""
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    """No discount strategy."""
    def apply_discount(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    """Apply a percentage discount."""
    def _init_(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percentage / 100)


class FixedAmountDiscount(DiscountStrategy):
    """Apply a fixed amount discount."""
    def _init_(self, amount: float):
        self.amount = amount

    def apply_discount(self, total: float) -> float:
        return max(total - self.amount, 0)



class Checkout:
    """Handles the checkout process with a discount strategy."""
    def _init_(self, cart: Cart, discount_strategy: DiscountStrategy):
        self.cart = cart
        self.discount_strategy = discount_strategy

    def get_final_total(self) -> float:
        total = self.cart.get_total_price()
        return self.discount_strategy.apply_discount(total)
    
    
    
    