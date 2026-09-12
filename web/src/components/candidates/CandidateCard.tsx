import type { Candidate } from "../../types/candidate";

type CandidateCardProps = {
    candidate: Candidate;
    selected?: boolean;
    onSelect?: () => void;
};

export default function CandidateCard(
    props: CandidateCardProps
) {
    return (
        <button
            class="candidate-card"
            classList={{
                selected: props.selected
            }}
            onClick={() => props.onSelect?.()}
        >
            <div class="candidate-avatar">
                {props.candidate.photo ? (
                    <img
                        src={props.candidate.photo}
                        alt={props.candidate.name}
                    />
                ) : (
                    <span>👤</span>
                )}
            </div>
            <strong>
                {props.candidate.name}
            </strong>
            {props.candidate.description && (
                <span>
                    {props.candidate.description}
                </span>
            )}
        </button>
    );
}
