type StatCardProps = {
    title: string;
    value: string | number;
    description?: string;
};

export default function StatCard(
    props: StatCardProps
) {
    return (
        <div class="stat-card">
            <span class="stat-title">
                {props.title}
            </span>
            <strong class="stat-value">
                {props.value}
            </strong>
            {props.description && (
                <span class="stat-description">
                    {props.description}
                </span>
            )}
        </div>
    );
}
