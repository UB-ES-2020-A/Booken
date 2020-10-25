import { createWebHistory, createRouter } from "vue-router";
import Front from "../components/Front.vue"
import Access from "../components/Access.vue"
import Location from "../components/Location.vue";

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
    path: "/location",
    name: "Location",
    component: Location,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;