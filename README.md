# 7water-creator-skills

**7wc = 7water Creator。** 一套给中文创作者使用的研究、选题、修稿和封面工作流。保留原版的理论研究、资料核查、语气约束与修稿细节；个人账号资料和私人保存路径由使用者自行配置。

| Skill | 用途 |
| --- | --- |
| [`7wc`](skills/7wc/README.md) | 总工作台。先了解创作者的领域、理论/思想立场、资料需求、受众与语气，再选择当前任务。 |
| [`topic-to-outline`](skills/topic-to-outline/README.md) | 从一句话题形成研究简报。按领域寻找理论、行业研报、学术研究、官方数据、政策或文本证据。 |
| [`writing-doctor`](skills/writing-doctor/README.md) | 按作者原声修稿。保留禁句扫描、20% 改动边界、标题—开头—正文兑现、证据、人味和口播自检。 |
| [`cover-maker`](skills/cover-maker/README.md) | 用已选真实图片制作封面，保留原标题与人物主体，处理构图、文字层级和成品比例。 |

## 使用

将所需的 `skills/<名称>/` 整个目录复制到 Agent 的 Skill 目录，保留 `SKILL.md`、`references/`、`scripts/` 和 `agents/` 的相对位置。四个 Skill 可以配合，也可单独使用。

```text
使用 $7wc：我主要讲商业与就业，倾向制度经济学，也想看行业研报。先帮我建立创作者研究底稿。
使用 $topic-to-outline：研究“留学生毕业后找工作”，比较学校官方数据和就业统计，再做内容简报。
使用 $writing-doctor：只修标题、开头和证据跳步，保留我原句与语气。
使用 $cover-maker：用这张图片和我的原标题做 3:4 与 4:3 封面。
```

首次使用 `7wc` 时，粗略说清：内容领域和读者、偏好的理论或意识形态视角、需要什么资料、希望保留的语气与表达习惯。不确定的项目可以写“待定”。[配置模板](skills/7wc/references/creator-profile.md)只作提示，不要求完整填表。按领域选择理论与来源可参考[研究地图](skills/topic-to-outline/references/domain-research-map.md)。

研究地图中的商业、小说、留学、女性成长等领域只是演示方法；遇到任何新领域，都按问题类型、理论视角和证据需求重新建立地图。

`writing-doctor` 保留原版较强的默认语气规则；作者可以在本轮说明自己的特例。固定频道介绍、CTA 四件套和归档位置须由作者提供或启用，不包含任何个人账号的私有配置。

研究时区分事实、理论解释与作者判断；不编造案例、数字和引语。许可协议：[MIT](LICENSE)。
