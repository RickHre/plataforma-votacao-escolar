import type { JSX } from "solid-js";

type InputProps =
    JSX.InputHTMLAttributes<HTMLInputElement> & {
        label?: string;
        error?: string;
    };

export default function Input(
    props: InputProps
) {
    return (
        <label class="input-group">
            {props.label && (
                <span class="input-label">
                    {props.label}
                </span>
            )}
            <input
                {...props}
                class={`input ${
                    props.class ?? ""
                }`}
            />
            {props.error && (
                <span class="input-error">
                    {props.error}
                </span>
            )}
        </label>
    );
}
