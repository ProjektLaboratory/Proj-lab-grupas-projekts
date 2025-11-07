# Proj-lab-grupas-projekts



## Līdzīgo risinājumu pārskats

**Samsung food: Meal Manager**
<br></br>
<img src="/images-for-similar-solution-comparison/Samsung-Food-Meal-Planner-image-1.png" />

<div align="top">
  <img width="648" height="1252.8" src="/images-for-similar-solution-comparison/Samsung-Food-Meal-Planner-image-2.png" />
  <img width="648" height="1249.2" src="/images-for-similar-solution-comparison/Samsung-Food-Meal-Planner-image-3.png" />
</div>


<br></br>
<br></br>

**Manage Meals**
<br></br>
<img src="/images-for-similar-solution-comparison/Manage-Meals-image-1.png" />

<div align="top">
  <img width="598" height="363" src="/images-for-similar-solution-comparison/Manage-Meals-image-2.png" />
  <img width="726" height="510" src="/images-for-similar-solution-comparison/Manage-Meals-image-3.png" />
</div>


Neder, jo
    1. tikai apskata produkta informāciju - Soosee, Open Food Facts
    2. tikai sniedz informāciju par restorāniem - AllergyEats



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
<br>
<br>@enduml



## Tehnoloģiju steks

<img width="280" height="801" src="/tehnologiju_steks.png">