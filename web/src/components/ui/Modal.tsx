import type { ParentProps } from "solid-js";

type ModalProps = ParentProps & {
    open: boolean;
    title: string;
    onClose: () => void;
};

export default function Modal(
    props: ModalProps
) {
    if (!props.open) {
        return null;
    }

    return (
        <div class="modal-backdrop">
            <div class="modal">
                <div class="modal-header">
                    <h2>{props.title}</h2>
                    <button
                        class="modal-close"
                        onClick={props.onClose}
                    >
                        ×
                    </button>
                </div>
                <div class="modal-body">
                    {props.children}
                </div>
            </div>
        </div>
    );
}
