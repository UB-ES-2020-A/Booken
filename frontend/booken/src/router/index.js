import {createWebHistory, createRouter} from "vue-router";
import Front from "../components/Front.vue"
import Access from "../components/Access.vue"
import Shopping_cart from "../components/Shopping_cart";
import BookInfo from "../components/BookInfo.vue"
import Contact from "../components/Contact";
import ShowBooks from "@/components/ShowBooks";

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
        path: "/cart",
        name: "ShoppingCart",
        component: Shopping_cart,
    },
    {
        path: "/book/:id",
        name: "BookInfo",
        component: BookInfo,
    },
    {
        path: "/contact",
        name: "Contact",
        component: Contact,
    },
    {
        path: "/books/:category",
        name: "books",
        component: ShowBooks,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;