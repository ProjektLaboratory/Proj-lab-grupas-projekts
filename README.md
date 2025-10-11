# Proj-lab-grupas-projekts


## Līdzīgo risinājumu pārskats


## Konceptu modelis

<img width="810" height="680" alt="image" src="https://github.com/user-attachments/assets/f9a1aace-b99a-4704-8478-d74f91dc5fe1" />

<br>@startuml
<br>skinparam linetype ortho
<br>
<br>
<br>class Person
<br>class Menu
<br>class Dish
<br>
<br>class DietType
<br>
<br>class Allergens
<br>class Recipes
<br>
<br>class Ingredients
<br>class nutritional_values {
<br>  calories
<br>  protein
<br>  carbs
<br>  fat
<br>}
<br>class Measurement
<br>
<br>class time_needed
<br>class Category
<br>class Cuisine
<br>
<br>
<br>Person "1"  -- "*" Menu
Menu "1"  -- "*" Dish
<br>
<br>Dish "*"  -- "*" DietType
<br>
<br>Dish "*"  -- "*" Allergens
<br>Dish "1"  -- "*" Recipes
<br>Recipes "*"  -- "*" Allergens
<br>
<br>Dish "*"  -- "*" Ingredients
<br>Dish "1"  -- "*" nutritional_values
<br>Ingredients "*"  -- "*" nutritional_values
<br>Ingredients "1"  -- "1" Measurement
<br>Recipes "*"  -- "*" Ingredients
<br>Allergens "*"  - "*" Ingredients
<br>
<br>Dish "*"  -- "1" Category
<br>Dish "1"  -- "1" time_needed
<br>Dish "*"  -- "1" Cuisine
<br>


## Tehnoloģiju steks
<br>
<br>@enduml
