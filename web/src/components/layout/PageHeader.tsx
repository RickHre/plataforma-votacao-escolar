import type { JSX } from "solid-js";

type PageHeaderProps = {
    title: string;
    description?: string;
    action?: JSX.Element;
};

export default function PageHeader(
    props: PageHeaderProps
) {
    return (
        <div class="page-header">
            <div>
                <h1>{props.title}</h1>
                {props.description && (
                    <p>{props.description}</p>
                )}
            </div>
            {props.action && (
                <div class="page-header-action">
                    {props.action}
                </div>
            )}
        </div>
    );
}
