import { createWebHistory, createRouter } from "vue-router";
import Front from "../components/Front.vue"
import Access from "../components/Access.vue"
import Shopping_cart from "../components/Shopping_cart";
const routes = [
  {
    path: "/",
    name: "Front",
    component: Front,
  },
  {
    path: "/access",
    name: "Access",
    component: Access,
  },
    {
    path: "/shoppingcart",
    name: "ShoppingCart",
    component: Shopping_cart,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;