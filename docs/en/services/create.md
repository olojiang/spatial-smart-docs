# Create an API service

Three entry points open **New service** (新建服务): **＋ New service** at the top of the service tree on the left, the blue **＋ New service** button at the top of the middle area, and **New service** in the empty state shown when **No service selected** (还没有选中服务).

<Shot src="/media/zh/service-new.png" caption="New service dialog" />

::: steps
1. [Select a space](/en/guide/space) first, then switch to the **Services** (服务) module.
2. Click any **New service** entry point. The only type for now is **API service** (API 服务): "An API endpoint for querying and adjusting data" (对数据进行查询与调整的 API 接口).
3. **Service name** (服务名称, optional): if left blank, it's named automatically based on its function.
4. **Endpoint function** (接口功能, required): describe what the endpoint does in one sentence, e.g. "Return foot-traffic line chart data for the given start and end time." **Create service** (创建服务) **becomes clickable only after you fill this in.**
5. **Method and path** (请求方式与路径): choose `POST` (default) or `GET`; the path defaults to `/api/v1/new-service` — rename it to something meaningful, such as `/api/v1/booth-flow`.
6. Click **Create service**.
:::

::: tip Writing a good endpoint function
Spell out the **input**, **processing logic**, and **output**, and the generated endpoint will be more accurate:

> Given **startTime and endTime (ISO 8601)**, extract foot-traffic data for that time range from the booth data, **aggregate it by hour**, and return **the series array for the line chart and the total headcount `total`**.
:::

The hint at the bottom reads: "After creation, keep refining it through conversation, and publish it from Versions" (创建后可通过对话继续调整，在「版本管理」中发布上线).

| Method | When to use it |
| --- | --- |
| `POST` | Many parameters, or arrays/objects to pass (recommended default) |
| `GET` | Simple, read-only queries that are easy to open directly in a browser |
