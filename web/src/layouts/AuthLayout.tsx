import type { ParentProps } from "solid-js";

export default function AuthLayout(
    props: ParentProps
) {
    return (
        <div class="auth-layout">
            <div class="auth-container">
                {props.children}
            </div>
        </div>
    );
} 
