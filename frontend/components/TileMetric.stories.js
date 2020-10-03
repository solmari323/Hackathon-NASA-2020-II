import { storiesOf } from '@storybook/vue'

storiesOf('TileMetric', module).add('Default', () => ({
  template:
    '<TileMetricDefault title="Subscribers" value="2543" difference="375" icon="fas fa-users" colour="bg-blue-500" />',
}))

storiesOf('TileMetric', module).add('Zero', () => ({
  template:
    '<TileMetricDefault title="Likes" value="0" difference="0" icon="fas fa-thumbs-up" colour="bg-purple-500" />',
}))

storiesOf('TileMetric', module).add('Negative', () => ({
  template:
    '<TileMetricDefault title="Views" value="43014" difference="-17626" icon="fas fa-play" colour="bg-teal-500" />',
}))

storiesOf('TileMetric', module).add('Loading', () => ({
  template: '<TileMetricLoading />',
}))

storiesOf('TileMetric', module).add('Error', () => ({
  template: '<TileMetricError />',
}))
