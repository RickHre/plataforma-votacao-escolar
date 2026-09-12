type ParticipationCardProps = {
    percentage: number;
};

export default function ParticipationCard(
    props: ParticipationCardProps
) {
    return (
        <div class="participation-card">
            <div class="participation-circle">
                <strong>
                    {props.percentage}%
                </strong>
            </div>
            <div>
                <span>Participação</span>

                <strong>
                    {props.percentage}%
                </strong>
            </div>
        </div>
    );
}
