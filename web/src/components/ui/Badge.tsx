import type { ParentProps } from "solid-js";

type BadgeProps = ParentProps & {
    variant?: "default" | "success" | "warning" | "danger";
};

export default function Badge(
    props: BadgeProps
) {
    return (
        <span
            class={`badge badge-${
                props.variant ?? "default"
            }`}
        >
            {props.children}
        </span>
    );
}
