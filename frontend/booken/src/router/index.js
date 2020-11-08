import {createWebHistory, createRouter} from "vue-router";
import Front from "../components/Front.vue"
import Access from "../components/Access.vue"
import BookInfo from "../components/BookInfo.vue"
import Contact from "../components/Contact";
import ShowBooks from "@/components/ShowBooks";
import ControlPanel from "@/components/ControlPanel";

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
    },
    {
        path: "/cp",
        name: "ControlPanel",
        component: ControlPanel
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;