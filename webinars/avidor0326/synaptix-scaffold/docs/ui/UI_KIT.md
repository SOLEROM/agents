# {{PROJECT_NAME}} — UI Kit

> **Required before frontend implementation.**  
> Owner: CPO/Designer

---

## 1) Design Principles

- **Consistency > creativity:** Reuse existing patterns/components.
- **Accessibility is not optional:** Keyboard nav + labels + contrast.
- **Mobile-first:** Every screen must work on mobile widths.
- **Performance-aware:** Avoid heavy client bundles and unnecessary re-renders.

---

## 2) Design Tokens

### 2.1 Colors

| Token | Usage | Value |
|-------|-------|-------|
| `--color-primary` | Primary actions, links | `{{#3B82F6}}` |
| `--color-primary-hover` | Primary hover state | `{{#2563EB}}` |
| `--color-secondary` | Secondary actions | `{{#6B7280}}` |
| `--color-background` | Page background | `{{#FFFFFF}}` |
| `--color-surface` | Card/component background | `{{#F9FAFB}}` |
| `--color-text` | Primary text | `{{#111827}}` |
| `--color-text-muted` | Secondary text | `{{#6B7280}}` |
| `--color-border` | Borders, dividers | `{{#E5E7EB}}` |
| `--color-error` | Error states | `{{#EF4444}}` |
| `--color-success` | Success states | `{{#22C55E}}` |
| `--color-warning` | Warning states | `{{#F59E0B}}` |

### 2.2 Typography

| Token | Usage | Value |
|-------|-------|-------|
| `--font-family` | Primary font | `{{Inter, system-ui, sans-serif}}` |
| `--font-family-mono` | Code, monospace | `{{JetBrains Mono, monospace}}` |
| `--font-size-xs` | Captions | 12px |
| `--font-size-sm` | Small text | 14px |
| `--font-size-base` | Body text | 16px |
| `--font-size-lg` | Subheadings | 18px |
| `--font-size-xl` | Headings | 24px |
| `--font-size-2xl` | Page titles | 32px |
| `--font-weight-normal` | Body | 400 |
| `--font-weight-medium` | Emphasis | 500 |
| `--font-weight-bold` | Headings | 700 |

### 2.3 Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight spacing |
| `--space-2` | 8px | Related elements |
| `--space-3` | 12px | Default gap |
| `--space-4` | 16px | Section padding |
| `--space-6` | 24px | Card padding |
| `--space-8` | 32px | Section margins |

### 2.4 Borders & Shadows

| Token | Value |
|-------|-------|
| `--radius-sm` | 4px |
| `--radius-md` | 8px |
| `--radius-lg` | 12px |
| `--radius-full` | 9999px |
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.1)` |
| `--shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` |

---

## 3) Accessibility Requirements (WCAG AA)

| Requirement | Standard | Notes |
|-------------|----------|-------|
| Color contrast | 4.5:1 minimum | Text on background |
| Focus visible | Required | All interactive elements |
| Touch targets | 44x44px minimum | Mobile-friendly |
| Alt text | Required | All meaningful images |
| Keyboard nav | Full support | Tab order logical |
| Screen reader | ARIA labels | Dynamic content announced |

---

## 4) Component States

### Interactive Elements

| State | Border | Background | Text |
|-------|--------|------------|------|
| Default | `--color-border` | `--color-surface` | `--color-text` |
| Hover | `--color-primary` | `--color-surface` | `--color-text` |
| Focus | `--color-primary` (2px) | `--color-surface` | `--color-text` |
| Active | `--color-primary` | `--color-primary` | white |
| Disabled | `--color-border` | `--color-background` | `--color-text-muted` |
| Error | `--color-error` | `--color-surface` | `--color-error` |
| Success | `--color-success` | `--color-surface` | `--color-success` |

---

## 5) Core Components

### Button Variants

| Variant | Usage |
|---------|-------|
| Primary | Main actions |
| Secondary | Alternative actions |
| Ghost | Tertiary actions |
| Danger | Destructive actions |

### Input Types

| Variant | Usage |
|---------|-------|
| Text | Single-line input |
| Textarea | Multi-line input |
| Select | Dropdown selection |
| Checkbox | Boolean toggle |
| Radio | Single selection from group |

### Patterns

- **Empty states:** Show what to do next (not just "No data")
- **Error states:** Human message + retry + link to logs
- **Loading states:** Skeleton or spinner with context
- **Long forms:** Progressive disclosure, autosave if risky

---

## 6) Responsive Breakpoints

| Token | Width | Target |
|-------|-------|--------|
| `--breakpoint-sm` | 640px | Mobile landscape |
| `--breakpoint-md` | 768px | Tablet |
| `--breakpoint-lg` | 1024px | Desktop |
| `--breakpoint-xl` | 1280px | Large desktop |

---

## 7) Localization (i18n)

| Property | LTR | RTL |
|----------|-----|-----|
| Text direction | `ltr` | `rtl` |
| Flex direction | `row` | `row-reverse` |
| Margins/Padding | `left/right` | `right/left` |
| Icons | Standard | Mirrored (directional) |

**Note:** Use logical properties (`margin-inline-start`) over physical (`margin-left`).

---

## 8) Tech Stack (Fill In)

| Component | Choice |
|-----------|--------|
| UI library | `{{shadcn/ui | MUI | Chakra | custom}}` |
| Styling | `{{Tailwind | CSS Modules | Styled Components}}` |
| Form lib | `{{react-hook-form | formik | none}}` |
| Data fetching | `{{tanstack-query | swr | fetch}}` |
| Icon library | `{{lucide-react | heroicons | custom}}` |

---

## 9) Change Control

- Any token change requires `[CPO]` review
- Any new UI library requires `[CTO]` approval
- Component additions should be documented here

---

*Last updated: {{DATE}}*
