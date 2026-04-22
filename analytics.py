import pandas as pd


def perform_analytics(df):
    visual_group = df.groupby(['style', 'background', 'dynamics', 'color', 'face']).agg({
        'ROI': 'mean',
        'CTR': 'mean'
    }).sort_values(by='ROI', ascending=False).reset_index()

    top_performer = visual_group.iloc[0]

    insight = (
        f"{top_performer['style'].upper()} | {top_performer['background'].upper()} | ROI: {top_performer['ROI']:.2f}")

    return visual_group, insight, top_performer