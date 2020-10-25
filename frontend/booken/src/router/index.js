import { createWebHistory, createRouter } from "vue-router";
import Front from "../components/Front.vue"
import Access from "../components/Access.vue"
import BookInfo from "../components/BookInfo.vue"
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
    path: "/book_info",
    name: "BookInfo",
    component: BookInfo,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;