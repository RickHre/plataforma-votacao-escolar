import type { ParentProps } from "solid-js";

type CardProps = ParentProps & {
    class?: string;
};

export default function Card(
    props: CardProps
) {
    return (
        <section class={`card ${props.class ?? ""}`}>
            {props.children}
        </section>
    );
}
