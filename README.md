# Khazix Skills 本地集成

这个仓库现在已经内置了来自 [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) 的两个 Skill，方便直接在支持 Agent Skills 的环境中安装和同步。

## 已包含的 Skill

- `hv-analysis`
- `khazix-writer`

仓库内的技能目录位于：

```text
.agents/skills/
```

对应结构：

```text
.agents/skills/hv-analysis/
.agents/skills/khazix-writer/
```

## 安装到当前机器

对于 Codex 兼容的 Skill 目录，目标路径是：

```text
~/.agents/skills/
```

执行下面的脚本即可把仓库中的 Skill 同步到当前用户目录：

```bash
bash scripts/install_khazix_skills.sh
```

脚本会覆盖同名目录，适合在你更新仓库后重复执行。

## 如何使用

安装完成后，支持 Agent Skills 的 Agent 会在合适的任务场景下自动加载这些 Skill。你也可以在对话里明确描述意图，例如：

- `请用 hv-analysis 研究一下 OpenAI`
- `请用 khazix-writer 把这份素材写成公众号长文`

## 关于“能不能执行这个 Skill”

可以分成两层理解：

1. **安装层面**：可以，这个仓库已经带上了 Skill 文件，并且可以同步到 `~/.agents/skills/`
2. **运行层面**：严格来说，Skill 不是一个独立二进制程序，而是一组会被 Agent 读取和遵循的结构化指令

也就是说，我不能像运行一个单独命令那样“启动 Skill 进程”，但我可以：

- 安装它
- 读取它的 `SKILL.md`
- 在后续执行任务时按它的规则工作

例如：

- `hv-analysis` 更像是一套深度研究工作流
- `khazix-writer` 更像是一套长文写作风格和质检规范

## 上游来源与许可证

- 上游仓库：`https://github.com/KKKKhazix/khazix-skills`
- 上游许可证：MIT
- 本仓库保留了一份许可证副本：`licenses/khazix-skills.LICENSE`
