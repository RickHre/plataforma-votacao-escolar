import type { JSX, ParentProps } from "solid-js";

type ButtonProps =
    ParentProps &
    JSX.ButtonHTMLAttributes<HTMLButtonElement> &
	{ variant?: "primary" | "secondary" | "danger"; };

export default function Button(
    props: ButtonProps
) {
    const variant = () => props.variant ?? "primary";

    return (
        <button
            {...props}
            class={`button button-${variant()} ${
                props.class ?? ""
            }`}
        >
            {props.children}
        </button>
    );
}
