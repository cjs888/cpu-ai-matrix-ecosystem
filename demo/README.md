# CPU AI Matrix Ecosystem

## Global Co-Build Next-Generation Universal AI

**Zero GPU · Zero Threshold · Infinite Professional Model Matrix · Public AI For All Mankind**

> Repository Short Description
> Next-generation universal-AI architecture. Abandon bloated GPU-powered giant models. Construct an ecosystem of countless lightweight, CPU-native professional small models, built upon unified scheduling and standard interfaces. 100% open global co-construction, belonging to all humanity.

---

## Slogan

> The future of AI is not bigger parameters, but infinite professional modular matrix.
> No GPU, No monopoly, No threshold, AI for everyone.
> Decentralized universal AI ecosystem built by all humans.

> 推翻显卡算力垄断，终结巨型大模型内卷。
> 以无数专精小模型矩阵，共建全人类免费通用AI新文明。

---

## Core Idea

We give up the existing development path that keeps increasing model parameters and relies on high-end graphics cards.

Instead of one single omnipotent giant model:

- Develop a large number of **independent, lightweight, domain-specialized small models that run natively on CPU**
- All models collaborate through series or parallel execution under coordination
- Combined as a huge, infinitely-expandable **AI Matrix Ecosystem**, capable of handling complex general-purpose tasks

### Only two fixed top-level ground rules (permanent, unchanged)

1. **Unified global scheduling mechanism**
   A shared scheduling core takes charge of task understanding, automatic task decomposition, model invocation control, serial-parallel workflow arrangement, result aggregation and resource recycling.

2. **Unified standard input-output interface**
   Every model inside this ecosystem complies with the same interface specification.
   Output from any model can be directly fed as input into another compatible model, supporting free combination and modular collaboration.

> Important community statement
> **Except the two core rules above, all other technical details are NOT predefined by any individual.**
> Specific system architectures, communication protocols, code specifications, training pipelines, deployment solutions and ecological governance mechanisms will be discussed, standardized, iterated and maintained together by the global open-source community.
> Everyone is free to propose schemes, carry out experiments and reach consensus collectively.

---

## Feasibility Statement

The core concept is technically feasible with a logically closed-loop design.
It provides a viable alternative evolutionary route to GPU-based large models.
Real-world engineering challenges remain, which are waiting for the whole community to solve step-by-step through practice.

### Main foreseeable challenges for future development

1. The global community needs sufficient communication to reach stable agreements on detailed protocols and standards; fragmentation may occur without consensus.
2. Balancing intelligence and hardware consumption of the scheduling core is a key research topic.
3. Multi-modal tasks (image, video) require continuous long-term optimization to achieve smooth pure-CPU inference.
4. CPU-based training has inherent speed limits, mostly suitable for small-scale personalized fine-tuning rather than large-scale full training.
5. Long-term community governance rules need to be established through collective negotiation.

None of these problems invalidate the core idea; they are engineering goals for all participants.

---

## Ideal Working Flow

(described conceptually, no concrete implementation locked-in)

1. User submits complex requests, which may contain text, images, parameters or mixed-modality content.
2. The unified scheduling core parses and splits the original task into multiple independent subtasks.
3. Corresponding professional small models are automatically scheduled to run in serial or parallel.
4. Multiple models cooperate and compute following their own domain logic.
5. The scheduling core aggregates all outputs and returns the final standardized result to the end-user.
6. System automatically releases occupied memory and computing resources after completion.

> Note: Only workflow logic is defined. Developers are free to choose programming languages, communication methods and storage implementations.

---

## Global Open-Source Community Declaration

This is NOT a personal, corporate or commercial project.
It is a public AI infrastructure owned by all mankind.

- No monopoly, no closed-source derivatives that lock the whole ecosystem.
- No commercial barriers restricting participation, modification or redistribution.
- Anyone can develop new domain-specific models, improve existing modules, propose architectural improvements and participate in standard-setting.
- Every industry can build its own professional AI module and integrate it into the matrix ecosystem.
- All technical standards are negotiated, voted on and iterated openly by global contributors.

**Openness, equality, co-construction and shared benefits are our everlasting principles.**

---

## Call For Global Contributors

We invite software engineers, AI researchers, industry practitioners, hobbyists and open-source enthusiasts all over the world.

Join this revolution to build:

**The world's first real universal AI matrix ecosystem, GPU-free, infinitely-evolvable and shared by all humans.**

> Old era: Giant models + GPU monopoly, bloated, expensive and lacking professional accuracy.
> New era: Professional small-model matrix + native-CPU operation, global co-construction, zero entry barrier and outstanding domain precision.

**The era of GPU-driven giant-model monopoly is fading away.
The era of global CPU AI-matrix public ecosystem is coming.**

---

## Permanent Open-Source Statement

This conceptual framework is permanently open-sourced, free of charge and open for global co-development.
All developers worldwide may take part in standard formulation, architecture optimization, model development and ecological iteration freely.
# Add demo architecture prototype
# Demo Prototype Readme
> ⚠️ **Important Declaration**
> This set of sample code is only an architectural prototype for community discussion.
> None of the interfaces, communication methods, and data structures defined in the code are official final standards.
> All formal specifications will be discussed, revised and finalized together by global open‑source contributors.
>
> 本套样本代码仅仅用于社区架构讨论的原型演示。
> 代码中写死的接口、通信方案、数据结构，**均不作为正式标准**。
> 一切正式规范，交由全球开源参与者共同讨论、修订、定稿。

## Project Positioning
CPU‑AI‑Matrix‑Ecosystem does not target any single industry.
It is a general‑purpose, CPU‑native collaborative AI infrastructure facing all human industries and scientific research scenarios.
Various vertical modules covering industry, science, engineering, culture, medical treatment, production, software development and other fields can be freely accessed into the matrix system.

项目定位：
CPU‑AI‑Matrix‑Ecosystem 不绑定任何单一行业。
它是一套面向人类全部产业、科研场景，原生基于CPU运行的通用协同AI基础设施。
覆盖工业、科研、工程、文创、医疗、生产、软件开发等不同领域的各类垂直模块，都可以自由接入这套矩阵系统。

## Logical 3‑Layer Architecture（逻辑三层架构，顶层架构长期稳定）
Client Layer (Client)
↓
Scheduler Core Layer (Scheduler)
↓
Micro‑Module Layer (MicroModule)
### Core invariable architectural constraints（两条永久不变架构约束）
1. All messages between modules **must be forwarded through the scheduler**. Modules cannot call each other directly.
2. Every task request and response must adopt a unified wrapped message envelope structure. The internal business payload can be freely defined by each module.

> 两条永久不变架构约束
> 1. 模块之间所有消息**必须经由调度器转发**，模块禁止直接互相调用。
> 2. 每一条任务请求、响应，都必须采用统一封装的消息信封结构；内部业务载荷 payload，可以由各个模块自由定义。

### Component responsibilities
#### 1. Client 客户端
- Responsible for user interaction, assemble the initial standard request message.
- Submit tasks to scheduler, receive and render final result data.
- Never invoke any micro‑module directly.

职责：负责人机交互，组装初始标准化请求报文；向调度器提交任务，接收并展示最终结果。**禁止直接调用任何微模块**。

#### 2. Scheduler 调度中枢（系统核心）
- Receive task message from client.
- Parse and split complex task into multiple independent subtasks.
- Route subtasks to corresponding target modules, support serial execution and parallel execution.
- Forward standard messages between client and modules, also between different modules.
- Collect execution results returned from each module, aggregate data into final output.
- Manage full task lifecycle: timeout control, exception capture, resource release notification.
- Scheduler itself shall not implement any domain‑specific business logic. All professional computation is completed inside micro‑modules.

职责：接收客户端任务；解析并拆分复杂任务为若干独立子任务；路由分发子任务到对应模块，支持串行、并行执行；在客户端、各个模块之间转发标准消息；收集全部模块返回的数据，聚合生成最终输出；完整管理任务生命周期：超时、异常捕获、通知资源释放。
**调度器本身不实现任何行业业务逻辑，所有专业运算全部交由微模块完成。**

#### 3. MicroModule 微模块
- Single responsibility principle: one module only solves one kind of professional problem.
- Stateless design as far as possible. After task finished, model resources can be unloaded.
- Only communicate with scheduler, unknown existence of other modules inside ecosystem.
- Receive standard message, run domain‑specific computing or AI inference, return a compliant standard message.
- Execute resource cleanup command sent from scheduler, release memory and loaded model weights.

职责：遵循单一职责，一个模块只解决一类专业问题；尽量做到无状态，任务结束之后可以卸载模型资源；仅和调度器通信，模块不知道生态内其他模块；接收标准消息，执行专业计算或者AI推理，返回合规的标准消息；执行调度器下发的资源清理指令，释放内存与已经加载的模型权重。

## Full data flow demonstration 完整数据流演示
1. Client constructs a complete standard message and sends it to Scheduler.
2. Scheduler parses the original task, splits it into several subtasks.
3. Scheduler distributes subtasks one by one or in parallel to corresponding micro‑modules.
4. Each micro‑module executes calculation, returns result message back to scheduler.
5. Scheduler aggregates all subtask results, packages final output message.
6. Final message is returned to Client for presentation.
7. Scheduler broadcasts resource‑release instruction, all related modules unload occupied resources.

> Path：`Client → Scheduler → Module‑A → Scheduler → Module‑B → Scheduler → Client`

## What is NOT enforced（不做强制规定，留给社区共同决策）
- Inter‑process communication: stdio, local socket, HTTP, gRPC, any solution can be discussed.
- Serialization format: JSON, MessagePack, Protobuf, waiting for community selection.
- Implementation scheme of task decomposition inside scheduler: rule‑based engine, lightweight local model or other algorithms.
- Module packaging, distribution, version management, public module repository.
- Distributed deployment, cross‑machine collaborative scheduling, load‑balancing strategy.
- Training, fine‑tuning workflow and supporting tool‑chain.

## Directory structure of demo prototype
```
demo/
├── README.md
├── message.py        # Standard message model
├── scheduler.py      # Minimal scheduler prototype
├── micro_module.py   # Abstract base class for all micro‑modules
├── example_modules/
│   ├── text_analyser.py
│   └── data_compute.py
├── client.py         # Simulation client
└── main.py           # Program entry, run end‑to‑end demo
```


## Run Instructions
```bash
cd demo
python main.py
Environment requirement: Python 3.8+, only standard library needed, no extra third‑party packages.
This demo only verifies the validity of top‑level collaboration architecture. All concrete standards remain to be discussed by community.

### ② demo/message.py
```python
import uuid
import time
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional


@dataclass
class MessageHeader:
    task_id: str
    from_module: str
    target_module: str
    timestamp: float
    status: str  # "success" / "fail"
    error_code: int
    error_msg: str


@dataclass
class MessageMeta:
    attachments: List[str]


@dataclass
class StandardMessage:
    """
    Unified envelope for all messages inside matrix ecosystem.
    Only the outer envelope structure is referenced as a prototype.
    All formal specifications need community joint discussion.
    """
    header: MessageHeader
    payload: Dict[str, Any]
    meta: MessageMeta

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def build(
        cls,
        from_id: str,
        target_id: str,
        payload: Dict[str, Any],
        task_id: Optional[str] = None,
        status: str = "success",
        error_code: int = 0,
        error_msg: str = "",
        attachments: Optional[List[str]] = None
    ) -> "StandardMessage":
        if task_id is None:
            task_id = str(uuid.uuid4())
        header = MessageHeader(
            task_id=task_id,
            from_module=from_id,
            target_id=target_id,
            timestamp=time.time(),
            status=status,
            error_code=error_code,
            error_msg=error_msg
        )
        meta = MessageMeta(attachments=attachments if attachments else [])
        return cls(header=header, payload=payload, meta=meta)
