// static/js/recipes-data.js
// Centralized recipes data used by home.html and recipe.html
window.RECIPES = [
  /* Breakfast (3) */
  {
    id: 'b1',
    cat: 'breakfast',
    title: 'Quick Omelette with Veggies',
    image: '/static/images/breakfast_omlete.jpg',
    short: 'A hearty omelette in 10 minutes.',
    description: 'Quick and tasty omelette with mixed vegetables.',
    ingredients: ['eggs', 'onion', 'mushrooms', 'bell pepper', 'salt', 'pepper', 'oil'],
    allergens: ['egg'],
    time: 10,
    mealType: 'breakfast',
    cuisine: 'international',
    steps: [
      'Chop the vegetables.',
      'Heat the pan and sauté vegetables until soft.',
      'Pour the beaten eggs and cook until set.'
    ]
  },

  {
    id: 'b2',
    cat: 'breakfast',
    title: 'Greek Yogurt Bowl',
    image: '/static/images/breakfast_greek_yogurt.jpg',
    short: 'Light bowl with fruits and granola.',
    description: 'A refreshing yogurt bowl with fresh fruits and crunchy granola.',
    ingredients: ['greek yogurt', 'fresh fruits', 'granola', 'honey'],
    allergens: ['milk', 'nuts'],
    time: 5,
    mealType: 'breakfast',
    cuisine: 'greek',
    steps: [
      'Put yogurt into a bowl.',
      'Top with sliced fruits and granola.',
      'Drizzle with honey and serve.'
    ]
  },

  {
    id: 'b3',
    cat: 'breakfast',
    title: 'Oatmeal with Banana',
    image: '/static/images/breakfast_oatmeal_banana.jpg',
    short: 'Warm oatmeal with bananas.',
    description: 'Comforting porridge topped with banana and cinnamon.',
    ingredients: ['oats', 'banana', 'milk or water', 'cinnamon'],
    allergens: ['milk'],
    time: 8,
    mealType: 'breakfast',
    cuisine: 'international',
    steps: [
      'Cook oats with milk or water according to package.',
      'Slice banana and place on top.',
      'Sprinkle with cinnamon and serve.'
    ]
  },

  /* Lunch (3) */
  {
    id: 'l1',
    cat: 'lunch',
    title: 'Caesar Salad',
    image: '/static/images/lunch_caesar.jpg',
    short: 'Classic romaine salad with creamy dressing.',
    description: 'Romaine lettuce with Caesar dressing, parmesan and croutons.',
    ingredients: ['romaine lettuce', 'parmesan', 'croutons', 'caesar dressing', 'anchovy (optional)'],
    allergens: ['milk', 'egg', 'fish'],
    time: 12,
    mealType: 'lunch',
    cuisine: 'italian',
    steps: [
      'Chop romaine lettuce.',
      'Toss with dressing, parmesan and croutons.',
      'Serve immediately.'
    ]
  },

  {
    id: 'l2',
    cat: 'lunch',
    title: 'Seasonal Vegetable Soup',
    image: '/static/images/lunch_veg_soup.jpg',
    short: 'Hearty seasonal soup.',
    description: 'Warm and healthy vegetable soup with seasonal produce.',
    ingredients: ['potatoes', 'carrot', 'celery', 'onion', 'broth'],
    allergens: [],
    time: 30,
    mealType: 'lunch',
    cuisine: 'latvian',
    steps: [
      'Chop vegetables into bite-size pieces.',
      'Sauté onion and garlic, add vegetables.',
      'Pour broth and simmer 20–30 minutes.'
    ]
  },

  {
    id: 'l3',
    cat: 'lunch',
    title: 'Tuna Sandwich',
    image: '/static/images/lunch_tuna_sandwich.jpg',
    short: 'Quick sandwich with tuna and veggies.',
    description: 'Classic tuna sandwich—fast and filling.',
    ingredients: ['canned tuna', 'bread', 'lettuce', 'mayonnaise'],
    allergens: ['fish', 'egg', 'gluten'],
    time: 6,
    mealType: 'lunch',
    cuisine: 'international',
    steps: [
      'Mix tuna with mayonnaise and seasoning.',
      'Spread on bread and add lettuce.',
      'Cut and serve.'
    ]
  },

  /* Dinner (3) */
  {
    id: 'd1',
    cat: 'dinner',
    title: 'Lemon Chicken Fillet',
    image: '/static/images/dinner_lemon_chicken.jpg',
    short: 'Juicy chicken with lemon and herbs.',
    description: 'Pan-fried chicken fillet with lemon and fresh herbs.',
    ingredients: ['chicken fillet', 'lemon', 'olive oil', 'thyme', 'salt', 'pepper'],
    allergens: [],
    time: 25,
    mealType: 'dinner',
    cuisine: 'international',
    steps: [
      'Prepare marinade with lemon and herbs.',
      'Pan-fry chicken until golden and cooked through.',
      'Finish with lemon juice and serve.'
    ]
  },

  {
    id: 'd2',
    cat: 'dinner',
    title: 'Stir Fried Veggie Pasta',
    image: '/static/images/dinner_stir_pasta.jpg',
    short: 'Colorful vegan pasta dish.',
    description: 'Quick stir-fried vegetables tossed with pasta.',
    ingredients: ['pasta', 'zucchini', 'bell pepper', 'tomatoes', 'olive oil'],
    allergens: ['gluten'],
    time: 20,
    mealType: 'dinner',
    cuisine: 'italian',
    steps: [
      'Cook pasta until al dente.',
      'Sauté vegetables until tender.',
      'Mix pasta with vegetables and serve.'
    ]
  },

  {
    id: 'd3',
    cat: 'dinner',
    title: 'Steamed Salmon with Dill Sauce',
    image: '/static/images/dinner_steamed_salmon.jpg',
    short: 'Healthy salmon with dill sauce.',
    description: 'Delicate steamed salmon served with a creamy dill sauce.',
    ingredients: ['salmon fillet', 'lemon', 'dill', 'salt'],
    allergens: ['fish'],
    time: 18,
    mealType: 'dinner',
    cuisine: 'scandinavian',
    steps: [
      'Steam the salmon until cooked through.',
      'Prepare dill sauce and season to taste.',
      'Serve salmon topped with sauce and lemon slices.'
    ]
  }
];

// Store into localStorage so home filter can use it (overwrites previous demo data)
try {
  localStorage.setItem('limpa_recipes_v1', JSON.stringify(RECIPES));
  console.log('✅ Recipes saved to localStorage (limpa_recipes_v1).');
} catch(e) {
  console.warn('⚠️ Could not write recipes to localStorage:', e);
}
