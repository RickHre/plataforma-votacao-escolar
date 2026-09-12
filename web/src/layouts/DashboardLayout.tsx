import type { ParentProps } from "solid-js";

import Sidebar from "../components/layout/Sidebar";
import Header from "../components/layout/Header";

export default function DashboardLayout(
    props: ParentProps
) {
    return (
        <div class="dashboard-layout">
            <Sidebar />
            <div class="dashboard-main">
                <Header />
                <main class="dashboard-content">
                    {props.children}
                </main>
            </div>
        </div>
    );
} 
